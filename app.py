from flask import Flask,jsonify

app=Flask(__name__)

books=[
    {"id":1,"name":"João"},
    {"id":2 ,"name":"Jonas "},
    {"id":3 ,"name":"Jerimundo "}
]

@app.route ("/books", methods=["GET"])
def home():
    return jsonify({"mensagem: ":"API de Usuarios"})

@app.route("/", methods=["GET"])
def listar_books():
    return jsonify(books)

if __name__ == "__main__":
    app.run(port=5001)