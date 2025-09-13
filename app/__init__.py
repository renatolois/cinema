import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

from app.utils import login_required


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')

    @app.route("/")
    def index():
        return render_template('index/index.html')

    @app.route("/login")
    def login():
        return "login page"

    @app.route("/home")
    @login_required
    def home():
        return render_template('home/home.html')

    @app.route("/profile")
    def profile():
        return "profile page"

    
    return app