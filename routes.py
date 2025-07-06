from flask import request, jsonify
from main import app
from db import db
from models import Cafes

@app.route('/api/cafes', methods=['GET'])
def listar_cafes():
    cafes = Cafes.query.all()
    return jsonify([
        {
            'id': cafe.id,
            'nome': cafe.nome,
            'produtor': cafe.produtor,
            'variedade': cafe.variedade,
            'sensorial': cafe.sensorial,
            'tipo': cafe.tipo,
            'regiao': cafe.regiao,
            'altitude': cafe.altitude
        } for cafe in cafes
    ])

@app.route('/api/cafes', methods=['POST'])
def adicionar_cafe():
    data = request.get_json()

    novo = Cafes(
        nome=data['nome'],
        produtor=data['produtor'],
        variedade=data['variedade'],
        sensorial=data['sensorial'],
        tipo=data['tipo'],
        regiao=data['regiao'],
        altitude=data['altitude']
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify({'mensagem': 'Café adicionado com sucesso'}), 201

@app.route('/api/cafes/<int:id>', methods=['GET'])
def detalhar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    return jsonify({
        'id': cafe.id,
        'nome': cafe.nome,
        'produtor': cafe.produtor,
        'variedade': cafe.variedade,
        'sensorial': cafe.sensorial,
        'tipo': cafe.tipo,
        'regiao': cafe.regiao,
        'altitude': cafe.altitude
    })

@app.route('/api/cafes/<int:id>', methods=['DELETE'])
def deletar_cafe(id):
    cafe = Cafes.query.get_or_404(id)
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({'mensagem': 'Café deletado com sucesso'}), 200
