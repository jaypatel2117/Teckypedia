"""
Authors: Rahul and Harshit
Created: 7th Dec, 2023
Modified: 15th Dec, 2023
Description: Module handling user authentication, including login, logout, and 
sign-up routes. Also includes an admin panel route for adding products to the 
e-commerce website.
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route.

    Handles user login, checks email and password validity,
    logs in the user if valid, and redirects to the home page.

    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    """
    Logout route.

    Logs out the currently logged-in user and redirects to the login page.

    """
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Sign-up route.

    Handles user registration, validates form data, and creates a new user
    if all information is valid. Logs in the new user and redirects to the home page.

    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first-name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match.", category="error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="error")
        else:
            # add user to the database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success") 
            return redirect(url_for('views.home'))
            
    return render_template("sign_up.html", user=current_user)


UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@auth.route('/admin-panel', methods=['GET', 'POST'])
def admin_panel():

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        file = request.files['file']

        if name and description and price and file:
            # Check if the file has an allowed extension
            if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
                # Save the product details to the database
                new_product = Product(name=name, description=description, price=float(price))

                # Save the image to the server and update the image_path
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)
                new_product.image_path = os.path.join('images', filename)  # Update this line

                db.session.add(new_product)
                db.session.commit()

                flash('Product added successfully!', category='success')
            else:
                flash('Invalid file format. Allowed formats are: png, jpg, jpeg, gif.', category='error')
        else:
            flash('Please fill in all the fields.', category='error')

    return render_template('admin_panel.html', user=current_user)

# @auth.route('/admin-login', methods=['GET', 'POST'])
# def admin_login():
#     if request.method == 'POST':
#         admin_id = request.form.get('admin_id')
#         password = request.form.get('password')

#         # Check if admin_id and password are 'admin'
#         if admin_id == 'admin' and password == 'admin':
#             # Create a dummy admin user for the session
#             dummy_admin_user = User(id=0, email='admin', password='admin', is_admin=True)
#             login_user(dummy_admin_user, remember=True)
#             flash('Admin logged in successfully!', category='success')
#             return redirect(url_for('auth.admin_panel'))

#         flash('Incorrect admin credentials, try again.', category='error')

#     return render_template("admin_login.html", user=current_user)

# @auth.route('/admin-panel')
# @login_required
# def admin_panel():
#     if current_user.is_admin:
#         print(current_user.is_admin)
#         return render_template('admin_panel.html', user=current_user)
#     else:
#         flash('Access denied. You are not an admin.', category='error')
#         return redirect(url_for('auth.admin_login'))

