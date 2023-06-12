from flask import Flask

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

# methods=['GET'] is a default method.
@app.route('/v1/users/idade/<nome>', methods=['GET']) 
def retorna_idade(nome: str):
    usuarios_filtrados = filter(lambda x: x["nome"] == nome.capitalize(), data["users"])
    idade = next(usuarios_filtrados, {"idade": None})["idade"]

    if nome:
         return { 'idade': idade }
    else:
    	return { 'idade': None }

app.run()
