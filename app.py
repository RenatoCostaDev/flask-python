from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<h1>Minha Primeira página</h1>'
app.run()

# O comando "set FLASK_APP=app" é usado para definir a variável de ambiente FLASK_APP
#  com o valor "app".
# o comando "flask run", o que inicia o servidor web Flask.