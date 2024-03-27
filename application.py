"""
Authors: Rahul, Harshit, Jay, and Kushal
Created: 15th Feb, 2024
Modified: 19th March, 2024
Description: Main entry point for the Techypedia e-commerce website. Initializes the Flask application using the create_app function from the 'website' module and runs the application in debug mode if executed directly.
"""

from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello_world():
  return "<p>Hello, World</p>"


if __name__ == '__main__':
  application.run(host='0.0.0.0', debug=True)
