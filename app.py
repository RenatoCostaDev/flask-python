from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Minha Primeira página</h1>'

@app.route('/segunda-pagina')
def segunda_pagina():
    return '<h1>Minha Segunda página</h1>'

@app.route('/form')
def form():
    return '''<form>
                <label>Primeiro nome:</label>
                <input type="text" placeholder="digite o seu primeiro nome"><br><br>\
                <label>Segundo  Nome:</label>
                <input type="text" placeholder="digite o seu segundo nome"><br><br>\
                <input type="submit" value="enviar">
            </form>'''


app.run()

# O comando "set FLASK_APP=app" é usado para definir a variável de ambiente FLASK_APP
#  com o valor "app".
# o comando "flask run", o que inicia o servidor web Flask.