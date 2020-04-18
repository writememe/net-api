"""
This file is the main engine of the web application

It initialises the Flask app, which exposes the swagger
API
"""

# Import module
from flask import render_template
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")

# Create a route to the base "/" page
@app.route("/")
def index():
    # Return the index.html template
    return render_template("index.html")


# Run the application
if __name__ == "__main__":
    app.run(debug=False)
