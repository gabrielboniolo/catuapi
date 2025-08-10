from flask import Flask
from db import db

# Inicializando app e db 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db.init_app(app)

from routes import *

# Execução do sistema
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)