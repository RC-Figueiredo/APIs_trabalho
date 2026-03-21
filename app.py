from flask import Flask,jsonify
import os

app=Flask(__name__)

books=[
    {"id":1,"name":"A volta ao mundo em 80 dias"},
    {"id":2 ,"name":"a arte da guerra "},
    {"id":3 ,"name":"megulho na escuridao "}
]

@app.route ("/books", methods=["GET"])
def home():
    return jsonify({"mensagem: ":"API de Livros"})

@app.route("/", methods=["GET"])
def listar_books():
    return jsonify(books)

if __name__ == "__main__": 
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)