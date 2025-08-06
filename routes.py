from app import app
from flask import request, jsonify

cafes = [
    {
        'id': 1,
        'nome': 'Melhor que chocolate',
        'produtor': 'Café ao Léo',
        'variedade': 'Blend',
        'sensorial': 'Chocolate'
    },
     {
        'id': 2,
        'nome': 'Melhor que chocolate',
        'produtor': 'Café ao Léo',
        'variedade': 'Blend',
        'sensorial': 'Chocolate'
    },
     {
        'id': 3,
        'nome': 'Melhor que chocolate',
        'produtor': 'Café ao Léo',
        'variedade': 'Blend',
        'sensorial': 'Chocolate'
    }
]

@app.route('/cafes', methods=['GET'])
def get_cafes():
    return jsonify(cafes)

@app.route('/cafes/<int:id>', methods=['GET'])
def get_cafe_id(id):
    for cafe in cafes:
        if cafe.get('id') == id:
            return jsonify(cafe)
        
@app.route('/edit_cafes/<int:id>', methods=['PUT'])
def edit_cafe(id):
    edit_cafe = request.get_json()
    for cafe in cafes:
        if cafe.get('id') == id:
            cafe.update(edit_cafe)
            return jsonify(cafe)
        
@app.route('/update_cafes', methods=['POST'])
def update_cafes():
    update_cafes = request.get_json()
    cafes.append(update_cafes)
    return jsonify(cafes)

@app.route('/delete_cafes/<int:id>', methods=['DELETE'])
def delete_cafes(id):
    for index, cafe in enumerate(cafes):
        if cafe.get('id') == id:
            del cafes[index]
            return jsonify(cafes)