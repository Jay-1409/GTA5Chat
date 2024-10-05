# GTA5 Chat

This project is for GTA-5 fans who want to interact with their favourite characters. It includes chat functionalities with over 10 different characters, offering an engaging experience for the community.

**[Live Demo](https://gta5chat-1.onrender.com/)**

## Features

- **Multiple Maps**: Explore different maps with interactive character dialogues.
- **Live Chat**: Chat live with various characters from GTA-5.
- **Video Transitions**: Enjoy seamless video transitions between different chat sessions.
- **Feedback Form**: Share your thoughts and help improve the platform.
- **Login System**: Secure login for user authentication.
- **10+ Characters**: Talk to over 10 unique GTA-5 characters, each with distinct dialogues.

## Screenshots / Demo

![App Screenshot 1](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/1.jpg)
![App Screenshot 2](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/2.jpg)
![App Screenshot 3](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/3.jpg)
![App Screenshot 4](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/4.jpg)
![App Screenshot 5](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/5.jpg)
![App Screenshot 6](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/6.jpg)

## Tech Stack

- **Backend**: Flask
- **API Integrations**: 
  - Gemini Generative API
  - Flask Libraries:
    - Flask==2.3.2
    - Flask-SQLAlchemy==3.0.4
    - Flask-Bcrypt==1.0.1
    - Flask-Login==0.6.3
    - Flask-WTF==1.2.1
    - WTForms==3.1.2
  - Google Generative AI (google-generativeai==0.7.2)
  - Gunicorn
  - Werkzeug (>=2.2.2)
  - Email Validator

## Project Structure

![Project Arrangement](https://raw.githubusercontent.com/harshpareshbhaigosalya/GTA5Chat/main/static/readmess/7.jpg)

- **Instance**: This folder contains the database files.
- **Static**: Contains images, videos, and music used in the website.
- **Templates**: Holds all the HTML templates for the website pages.

## How to Run the Project Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/harshpareshbhaigosalya/GTA5Chat.git
   ```
2. Navigate to the project directory:
   ```bash
   cd GTA5Chat
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the Flask application:
   ```bash
   python app.py
   ```
7. Open your browser and go to `http://127.0.0.1:5000/` to see the project.

