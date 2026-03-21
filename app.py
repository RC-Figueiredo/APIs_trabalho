from flask import Flask, jsonify
import os

app = Flask(__name__)

filmes= [
    {"id":1,"nome":"velozes e furiosos"},
    {"id":2,"nome":"terremoto a falha de san andreas"},
]

@app.route("/filme", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de filmes"})

@app.route("/", methods=["GET"])
def listar_filmes():
    return jsonify(filmes)


if __name__ == "__main__": 
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)