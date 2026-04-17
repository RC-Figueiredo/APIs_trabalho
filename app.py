from flask import Flask,jsonify

app=Flask(__name__)

jogos=[
    {"id":1,"name":"Far Cry"},
    {"id":2 ,"name":"The Crew"},
    {"id":3 ,"name":"Mario Bros "}
]

@app.route ("/jogos", methods=["GET"])
def home():
    return jsonify({"mensagem: ":"API de jogos"})

@app.route("/", methods=["GET"])
def listar_books():
    return jsonify(jogos)

if __name__ == "__main__":
    app.run(port=5001)