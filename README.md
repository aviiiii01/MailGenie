# MailGenie
MailGenie is an intelligent email assistant that generates and sends professional or friendly emails automatically based on user-provided context. 🚀
Whether to make a professional mail or friendly mail it makes your work easy and helps to save your time


# 🚀 Features
1:- AI-Generated Emails – Generates professional or friendly emails based on the provided context.
2:- Customizable Email Tone – Choose between Professional or Friendly tone.
3:- Secure Email Sending – Uses SMTP with SSL encryption for safe email delivery.
4:- Streamlit UI – User-friendly interface for inputting email details.

# 🛠️ Tech Stack
1:- Python
2:- Streamlit (Frontend)
3:- LangChain (Google Gemini AI for email generation)
4:- SMTP (for sending emails)
5:- Regular Expressions (re) (for extracting subject & body)


# Installation & Setup

1. Clone the Repository:
    https://github.com/aviiiii01/MailGenie.git
2. Navigate to the Project Directory:
    cd MailGenie
3. Create a Virtual Environment (Optional but Recommended):
    python -m venv venv
    source venv/bin/activate   # For macOS/Linux
    venv\Scripts\activate      # For Windows
4. Install Dependencies:
    pip install -r requirements.txt
5. In place for GEMINI_API_KEY write your api key generated from gemini studio. 
6. Run the Chatbot:
    streamlit run main.py
# Note
1. Make sure to add gemini api in place of "GEMINI_API_KEY" .
2. In password column of streamlit UI write the app password instead of gmail password.
    To create app password:-
    1. Go to manage your account from which you want to send mails.
    2. Then check whether 2 Step Verification is on or not if not then on it.
    3. Then in the search bar write app password.
    4. Create app and copy the password generated and paste in the password column of streamlit UI.

# Troubleshooting

1:-ModuleNotFoundError: No module named 'langchain'
    Ensure you installed dependencies with pip install -r requirements.txt.
    Try manually installing LangChain:
        pip install langchain
2:-ModuleNotFoundError: No module named 'langchain_community'
    Ensure you installed dependencies with pip install -r requirements.txt.
    Try manually installing LangChain_community:
        pip install langchain_community

# Contributing

Feel free to fork the repository and submit pull requests for improvements.

# License

This project is licensed under the MIT License.

