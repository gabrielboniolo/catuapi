from flask import render_template, request, redirect, url_for
from main import app
from db import db
from models import Cafes

@app.route('/')
def index():
    cafes = db.session.query(Cafes).all()
    return render_template('index.html', cafes=cafes)

@app.route('/registrar', methods=['GET', 'POST'])
def registrar_cafe():
    if request.method == 'GET':
        return render_template('registrar_cafe.html')
    elif request.method == 'POST':
        nome = request.form['nome']
        produtor = request.form['produtor']
        variedade = request.form['variedade']
        sensorial = request.form['sensorial']
        tipo = request.form['tipo']
        regiao = request.form['regiao']
        altitude = request.form['altitude']

        novo_cafe = Cafes(
            nome=nome,
            produtor=produtor,
            variedade=variedade,
            sensorial=sensorial,
            tipo=tipo,
            regiao=regiao,
            altitude=altitude
        )

        db.session.add(novo_cafe)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/cafe/<int:id>')
def visualizar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    return render_template('detalhe_cafe.html', cafe=cafe)

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('index'))
