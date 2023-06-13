from flask import Flask, render_template

data = {
	"users" : [
        {
            "nome": "Joao",
            "idade": 24
        },
        {
            "nome": "Francisco",
            "idade": 27
        }
    ]
}

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')

app.run()

# methods=['GET'] is a default method.
# @app.route('/v1/users/idade/<nome>', methods=['GET']) 
# def retorna_idade(nome: str):
#     usuarios_filtrados = filter(lambda x: x["nome"] == nome.capitalize(), data["users"])
#     idade = next(usuarios_filtrados, {"idade": None})["idade"]

#     if nome:
#          return { 'idade': idade }
#     else:
#     	return { 'idade': None }

