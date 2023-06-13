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

app.run(debug=True)


