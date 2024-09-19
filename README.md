
Ensure that your system has the latest versions of Python and pip installed. You can check this by running:

python --version
pip --version

Setup Instructions:
1. Clone the Repository
    git clone https://github.com/prasathkumara/AI-ChatBot.git

2. Set Up the Virtual Environment
    python -m venv rasa_env
    rasa_env\Scripts\Activate

Running the Chatbot

Train the chatBot
    rasa train (or) python -m rasa train

Command Line Interface
To run the chatbot in the command line interface, use:
    rasa shell (or) python -m rasa shell

Web Interface
To run the chatbot with a web interface and enable the API, use:

    rasa run --enable-api --cors "*" (or) python -m rasa run --enable-api --cors "*"

Running Custom Actions
    rasa run actions (or) python -m rasa run actions