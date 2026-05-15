from flask import Flask,jsonify
from flask import jsonify
from flask import request
from flask_cors import CORS

app=Flask(__name__)
 
CORS(app)

usuarios=[
    {"id":1,"name":"João"},
    {"id":2 ,"name":"Jonas "},
    {"id":3 ,"name":"Jerimundo "}
]


@app.route("/usuarios", methods=["GET"])
def buscar_usuarios():

    return jsonify(usuarios)


@app.route("/usuarios", methods=["POST"])
def cadastrar_usuario():

    novo_usuario = request.json

    usuarios.append(novo_usuario)

    return jsonify({
        "mensagem": "Usuário cadastrado!",
        "usuario": novo_usuario
    })



@app.route("/usuarios/<int:id>", methods=["PUT"])
def atualizar_usuario(id):

    dados = request.json

    for usuario in usuarios:

        if usuario["id"] == id:

            usuario["nome"] = dados["nome"]

            return jsonify({
                "mensagem": "Usuário atualizado!",
                "usuario": usuario
            })

    return jsonify({
        "mensagem": "Usuário não encontrado"
    })



@app.route("/usuarios/<int:id>", methods=["DELETE"])
def excluir_usuario(id):

    for usuario in usuarios:

        if usuario["id"] == id:

            usuarios.remove(usuario)

            return jsonify({
                "mensagem": "Usuário removido!"
            })

    return jsonify({
        "mensagem": "Usuário não encontrado"
    })


app.run(debug=True)