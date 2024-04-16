"""
Authors: Rahul
Created: 7th Dec, 2023
Modified: 15th Dec, 2023
Description: Blueprint for defining views and rendering templates for the Techypedia e-commerce website.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Create a Blueprint named 'views'
views = Blueprint('views', __name__)


@views.route('/')
def home():
  """
    Home route.

    Renders the home page template with the current user information.

    Returns:
        str: Rendered HTML template for the home page.
    """
  return render_template('home.html', user=current_user)


@views.route('/about')
def about():
  """
    About route.

    Renders the about page template with the current user information.

    Returns:
        str: Rendered HTML template for the about page.
    """
  return render_template('about.html', user=current_user)


@views.route('/admin-panel')
@login_required
def admin():
  """
    Admin panel route.

    Renders the admin panel page template with the current user information.
    Requires the user to be logged in.

    Returns:
        str: Rendered HTML template for the admin panel page.
    """
  return render_template('admin_panel.html', user=current_user)


@views.route('/cart')
@login_required
def cart():
  """
    Cart route.
    Renders the admin panel page template with the current user information.
    Requires the user to be logged in.
  
    Returns:
        str: Rendered HTML template for the admin panel page.
    """
  return render_template('cart.html', user=current_user)


@views.route('/product')
def product():
  """
  Product route.

  Renders the product page template with to show the detailed information     about the product.

  Returns:
      str: Rendered HTML template for the product page.
  """
  return render_template('product.html', user=current_user)


@views.route('/checkout')
def checkout():
  """
  Checkout route.

  Renders the checkout page with add and edit options.
  Requires the user to be logged in.

  Returns:
      str: Rendered HTML template for the checkout page.
  """
  return render_template('checkout.html', user=current_user)


@views.route('/order_confirmation')
def order_confirmation():
  """
  Checkout route.

  Renders the checkout page with add and edit options.
  Requires the user to be logged in.

  Returns:
      str: Rendered HTML template for the checkout page.
  """
  return render_template('order_confirmation.html', user=current_user)
