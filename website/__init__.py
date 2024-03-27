"""
Authors: Rahul and Harshit
Created: 7th Dec, 2023
Modified: 15th Dec, 2023
Description: Module responsible for creating the Flask application, configuring the database, and handling user authentication.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager 

# Define the SQLAlchemy database instance
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jqgedshad hasgdajg'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import views and auth blueprints
    from .views import views
    from .auth import auth

    # Register blueprints with the application
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import models and create the database tables
    from .models import User, CartItem, Product

    with app.app_context():
        db.create_all()
    
    # Configure and initialize Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def create_database(app):
    """
    Create the database if it doesn't exist.

    Args:
        app (Flask): The Flask application.
    """
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print('Created Database!')
