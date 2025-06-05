import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Console
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)

# Switch database based on environment
if os.getenv("FLASK_ENV") == "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB max

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
    if request.method != 'POST':
        return render_template('add_console.html')
    
    name = request.form['name']
    manufacturer = request.form['manufacturer']
    release_year = request.form['release_year']
    image = request.files.get('image')
        
    # Handle image upload
    image_filename = None
    if image and image.filename:
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        image_filename = filename
        
    # Create a new Console instance
    new_console = Console(
        name=name, 
        manufacturer=manufacturer, 
        release_year=release_year,
        image_filename=image_filename
    )

    # Add the new console to the database    
    db.session.add(new_console)
    db.session.commit()

    return redirect(url_for('view_consoles'))
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)