import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Console
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Switch database based on environment
if os.getenv("FLASK_ENV") == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('view_consoles'))

@app.route('/consoles')
def view_consoles():
    consoles = Console.query.all()
    return render_template('view_consoles.html', consoles=consoles)

@app.route('/consoles/add', methods=['GET', 'POST'])
def add_console():
    if request.method == 'POST':
        name = request.form['name']
        manufacturer = request.form['manufacturer']
        release_year = request.form['release_year']
        new_console = Console(name=name, manufacturer=manufacturer, release_year=release_year)
        db.session.add(new_console)
        db.session.commit()
        return redirect(url_for('view_consoles'))
    return render_template('add_console.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)