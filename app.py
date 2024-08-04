from flask import Flask, render_template, request, jsonify, redirect, url_for, flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import os
from urllib.parse import quote
import pickle

#global vars
eemail=''


#render


last_index_page = "index"
def logo_click():
    global last_index_page
    return redirect(url_for(last_index_page))
# Configure the Flask application
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the random string'    
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')  # Ensure to replace 'your_secret_key' with a real key or set it in your environment
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Configure the Gemini API
genai.configure(api_key="AIzaSyAdhHba59C82frkiMmR0U1a5YzfFuYm8DM")  # Replace with your actual API key

# Define characters
characters = {
    "character1": "Franklin",
    "character2": "Michael",
    "character3": "Trevor",
    "character4": "Lester",
    "character5": "Amanda", #
    "character6": "Ron",
    "character7": "Lazlow", #
    "character8": "Lamar",
    "character9": "Jimmy",
    "character10": "Tracey", #
    "character11": "Packie",
    "character12": "Devin",
    "character13": "Steve",
}

# Initialize the Gemini AI model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# File settings
def create_files(email):
    for character in characters:
        with open(f"{email}_{characters[character]}.pkl","wb") as file:
            pickle.dump([],file)
            
def append_data(character):
    email = eemail
    data = chat_session.history
    with open(f"{email}_{character}.pkl","wb") as file:
            pickle.dump(data,file)
    
def read_data(character):
    email=eemail
    with open(f"{email}_{character}.pkl","rb") as file:
        return pickle.load(file)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Forms
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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

# Routes
@app.route('/')
def index():
    session['last_index_page'] = 'index'
    return render_template('index.html')

@app.route('/index2.html')
def index2():
    session['last_index_page'] = 'index2'
    return render_template('index2.html')

@app.route('/index3.html')
def index3():
    session['last_index_page'] = 'index3'
    return render_template('index3.html')

@app.route('/index4.html')
def index4():
    session['last_index_page'] = 'index4'
    return render_template('index4.html')

@app.route('/character_page')
def character_page():
    return render_template('character_page.html')

@app.route('/logo_click')
def logo_click():
    last_index_page = session.get('last_index_page', 'index')
    return redirect(url_for(last_index_page))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        create_files(user.email)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            global eemail
            eemail = user.email
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/chat/<character>')
@login_required
def chat_character(character):
    if character in characters:
        global chat_session
        chat_session = initialize_chat_session(characters[character])
        return render_template('chat_character1.html', character=characters[character])
    else:
        return render_template('error.html', error_message="Character not found"), 404

@app.route('/chat', methods=['POST'])
@login_required
def chat_response():
    global chat_session
    message = request.form['message']

    # Send the user's message to the Gemini AI model
    response = chat_session.send_message(message)
    response_text = response.text.strip()

    # Return the AI's response as JSON
    return jsonify({'response': response_text})

# @app.route('/logo_click')
# def logo_click():
#     global last_index_page
#     return redirect(url_for(last_index_page))

@app.route('/Character_cards')
def Character_cards():
    return render_template('character_cards.html')

@app.route('/update_last_index/<page>')
def update_last_index(page):
    global last_index_page
    if page in ["index", "index2"]:
        last_index_page = page
    return '', 204  # No content response

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/save_changes', methods=['POST'])
def save_changes():
    # Retrieve data from the request
    data = request.json
    character = data.get('character')
    # Perform your save logic here
    append_data(character)
    # For demonstration, let's just print the data
    print(f"Data received: {data}")
    # Respond to the client
    return jsonify({"message": "Changes saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
