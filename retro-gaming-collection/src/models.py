from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    image_filename = db.Column(db.String(255))  # New field for image filename