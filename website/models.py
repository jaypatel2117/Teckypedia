"""
Authors: Rahul and Harshit
Created: 7th Dec, 2023
Modified: 15th Dec, 2023
Description: Module containing the database models for the Techypedia e-commerce website, including 'Product', 'User', and 'CartItem'.
"""

from . import db
from flask_login import UserMixin

class Product(db.Model):
    """
    Model representing a product in the e-commerce website.

    Attributes:
        id (int): Primary key for the product.
        name (str): Name of the product.
        image_path (str): Path to the product image.
        description (str): Description of the product.
        price (float): Price of the product.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image_path = db.Column(db.String(255))
    description = db.Column(db.Text)
    price = db.Column(db.Float)

class User(db.Model, UserMixin):
    """
    Model representing a user in the e-commerce website.

    Attributes:
        id (int): Primary key for the user.
        email (str): Email address of the user (unique).
        password (str): Hashed password of the user.
        first_name (str): First name of the user.
        is_admin (bool): Flag indicating whether the user is an admin (default is False).
        cart_items (relationship): Relationship representing products added to the user's cart.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    is_admin = db.Column(db.Boolean, default=False)
    cart_items = db.relationship('CartItem')

class CartItem(db.Model):
    """
    Model representing an item in the user's cart.

    Attributes:
        id (int): Primary key for the cart item.
        quantity (int): Quantity of the product in the cart.
        product_id (int): Foreign key referencing the associated product.
        user_id (int): Foreign key referencing the associated user.
        product (relationship): Relationship representing the associated product.
        user (relationship): Relationship representing the associated user.
    """
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product = db.relationship('Product')
    user = db.relationship('User')
