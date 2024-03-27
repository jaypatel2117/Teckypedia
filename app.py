"""
Authors: Rahul, Harshit, Jay, and Kushal
Created: 15th Feb, 2024
Modified: 19th March, 2024
Description: Main entry point for the Techypedia e-commerce website. Initializes the Flask application using the create_app function from the 'website' module and runs the application in debug mode if executed directly.
"""

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
