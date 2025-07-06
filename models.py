from db import db

class Cafes(db.Model):
    __tablename__ = 'cafes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), nullable=False)
    produtor = db.Column(db.String(40), nullable=False)
    variedade = db.Column(db.String(40), nullable=False)
    sensorial = db.Column(db.String(40), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    regiao = db.Column(db.String(40), nullable=False)
    altitude = db.Column(db.String(40), nullable=False) 