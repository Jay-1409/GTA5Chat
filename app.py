from flask import Flask, render_template, request, jsonify
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import google.generativeai as genai

# Configure the Flask application
app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key="AIzaSyAdhHba59C82frkiMmR0U1a5YzfFuYm8DM")  # Replace with your actual API key

# Define characters
characters = {
    "character1": "Franklin",
    "character2": "Michael",
    "character3": "Trevor"
}

# Initialize the Gemini AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Function to initialize chat session with the selected character
def initialize_chat_session(character_name):
    return genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
        system_instruction=f"""you are {character_name} from GTA 5 and now chat with me like that character. You have to behave exactly like the particular character
        If someone asks you for your name, then reply with your appropriate name.
        If someone asks you for your age, then reply with your appropriate age.
        If someone asks you for your gender, then reply with your appropriate gender.
        Also, do not reply to any questions that are not related to the game; instead, just say something like "You think I am an idiot asking such obvious questions."""
    ).start_chat(history=[])

# Route for rendering HTML templates
@app.route('/')
def index():
    return render_template('index.html', characters=characters)

@app.route('/index2.html')
def index2():
    return render_template('index2.html', characters=characters)

# Route for selecting a character and starting a chat session
@app.route('/chat/<character>')
def chat_character(character):
    if character in characters:
        global chat_session
        chat_session = initialize_chat_session(characters[character])
        return render_template('chat_character1.html', character=characters[character])
    else:
        return render_template('error.html', error_message="Character not found"), 404

# Route for handling chat messages
@app.route('/chat', methods=['POST'])
def chat_response():
    global chat_session
    message = request.form['message']

    # Send the user's message to the Gemini AI model
    response = chat_session.send_message(message)
    response_text = response.text.strip()

    # Return the AI's response as JSON
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
