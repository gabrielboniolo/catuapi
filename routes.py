from flask import request, jsonify, render_template, redirect, url_for
from db import db
from main import app
from models import Cafes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cafes', methods=['GET'])
def listar_cafes():
    cafes = db.session.query(Cafes).all()
    return render_template('listar_cafes.html', cafes=cafes)

@app.route('/cafes/<int:id>', methods=['GET'])
def listar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    return render_template('detalhar_cafe.html', cafe=cafe) 

@app.route('/cadastrar_cafes', methods=['GET', 'POST'])
def adicionar_cafe():
    if request.method == 'GET':
        return render_template('cadastrar_cafe.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        produtor = request.form['produtorForm']
        variedade = request.form['variedadeForm']
        sensorial = request.form['sensorialForm']
        tipo = request.form['tipoForm']
        regiao = request.form['regiaoForm']

        cafe = Cafes(
            nome=nome,
            produtor=produtor,
            variedade=variedade,
            sensorial=sensorial,
            tipo=tipo,
            regiao=regiao
        )

        db.session.add(cafe)
        db.session.commit()
        return redirect(url_for('listar_cafes'))

@app.route('/cafes/<int:id>/deletar', methods=['POST'])
def deletar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for('listar_cafes'))
