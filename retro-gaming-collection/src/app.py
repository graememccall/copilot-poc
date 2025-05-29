from flask import Flask
from db import init_db
from routes import register_routes

app = Flask(__name__)

# Initialize the database
init_db()

# Register routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)