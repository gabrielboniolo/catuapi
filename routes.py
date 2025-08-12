from flask import request, render_template, redirect, url_for 
from app import app
from db import db
from models import Cafe


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        nome = request.form('form_nome')
        produtor = request.form('form_produtor')
        variedade = request.form('form_variedade')
        sensorial =  request.form('form_sensorial')

        cafe = Cafe(
            nome=nome, 
            produtor=produtor, 
            variedade=variedade, 
            sensorial=sensorial
            )
        
        db.session.add(cafe)
        db.session.commit()

        return redirect(url_for('index'))
    

# @app.route('/cafes', methods=['GET'])
# def get_cafes():
#     return jsonify(cafes)

# @app.route('/cafes/<int:id>', methods=['GET'])
# def get_cafe_id(id):
#     for cafe in cafes:
#         if cafe.get('id') == id:
#             return jsonify(cafe)
        
# @app.route('/edit_cafes/<int:id>', methods=['PUT'])
# def edit_cafe(id):
#     edit_cafe = request.get_json()
#     for cafe in cafes:
#         if cafe.get('id') == id:
#             cafe.update(edit_cafe)
#             return jsonify(cafe)
        
# @app.route('/update_cafes', methods=['POST'])
# def update_cafes():
#     update_cafes = request.get_json()
#     cafes.append(update_cafes)
#     return jsonify(cafes)

# @app.route('/delete_cafes/<int:id>', methods=['DELETE'])
# def delete_cafes(id):
#     for index, cafe in enumerate(cafes):
#         if cafe.get('id') == id:
#             del cafes[index]
#             return jsonify(cafes)