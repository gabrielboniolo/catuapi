from db import db

class Cafe(db.Model):
    __tablename__ = 'cafes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    produtor = db.Column(db.Integer, nullable=False)
    variedade = db.Column(db.Integer, primary_key=True)
    sensorial = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<{self.nome}>'