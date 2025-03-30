from email.message import EmailMessage
import ssl#Secure Sockets Layer
import smtplib
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import re



from dotenv import load_dotenv

# if "memory" not in st.session_state:
#     st.session_state.memory = ConversationBufferMemory(
#         memory_key="chat_history", 
#         return_messages=True
#     )

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") 


st.set_page_config("Mail Botty!")
st.header("Write the context of the mail And the Mails of the Recievers")
ml=st.text_input("Enter your mail...! ")
passw=st.text_input("Enter your app password (go to manage your account and create 'app password'):", type="password")
context=st.text_input("Write the Context of the mail....")
maill=st.text_input("Write the mails of the recievers here separated with comma ','.....")
tone=st.radio("Select Email tone: ",["Proffesional","Friendly"])
# if(context and maill):
#     text_splitter=CharacterTextSplitter(
#         separator="\n",
#         chunk_size=10,
#         chunk_overlap=5,
#         length_function=len,
#     )
#     chunks = text_splitter.split_text(maill)
#     embeddings = HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L6-v2")
#     vectorstore=FAISS.from_texts(texts=chunks,embedding=embeddings)
llm=ChatGoogleGenerativeAI(model="gemini-2.0-pro-exp-02-05",api_key=GEMINI_API_KEY,temperature=0.7)#"gemini-2.0-flash"

# qa_chain=ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     retriever=vectorstore.as_retriever(),
#     memory=st.session_state.memory,
#     chain_type="stuff"
# )
# response = qa_chain({"question": context})
# st.write(response["answer"])
# st.write(maill)

prompt = f"Generate an email with only the subject, body, salutation and Closing/Complimentary Closing for a {tone.lower()} email based on the following context:\n{context}\nFormat: \nSubject: <Subject>\nBody: <Body>"
response=llm.invoke(prompt)
st.subheader("Generated Email Content:")
st.write(response.content)
email_content = str(response.content)

lst=maill.split(',')
SENDER_MAIL=os.getenv("SENDER_MAIL")
sender=ml
password=passw
subject_match = re.search(r"Subject:\s*(.+)", email_content)
body_match = re.search(r"Body:\s*(.+)", email_content, re.DOTALL)

subject = subject_match.group(1).strip() if subject_match else "No Subject"
body = body_match.group(1).strip() if body_match else email_content.strip()

for i in lst:
    x=EmailMessage()
    x["to"]=i
    x["from"]=sender
    x["subject"]=subject
    x.set_content(body)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL(host='smtp.gmail.com',port=465,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,i,x.as_string())
        st.success(f"Email sent to {i} successfully...")




