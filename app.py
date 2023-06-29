from flask import Flask, render_template, request, redirect, url_for
from utils import *

contatos_list = []

app = Flask(__name__)



# lesson5 routes

@app.route("/contatos")
def contatos():
    return render_template(
        'contatos.html',
        contatos_list=contatos_list,
        zip=zip,
    )

@app.route("/adicionar-contato", methods=['GET', 'POST'])
def contatos_form():
    if request.method == 'POST':
        if request.form.get('nome') and request.form.get('celular') and request.form.get('email'):
            contatos_list.append({
               'nome': request.form.get('nome'),
               'celular': request.form.get('celular'),
               'email': request.form.get('email'),
            })
            return redirect('/contatos')
    return render_template(
        'cadastro.html',
    )

@app.route("/<email>/deletar_contato", methods=['GET', 'POST'])
def deletar_contato(email):
    for i in range(len(contatos_list)):
        if contatos_list[i]['email'] == str(email): #Verifica o email recebido
            contatos_list.pop(i)
        return redirect('/contatos')
    app.run()

@app.route("/<email>/atualiza_contato", methods=['GET', 'POST'])
def atualiza_contato(email):
    contato = get_contact_by_email(email, contatos_list)
    if request.method == 'POST':
        contato['nome'] = request.form['nome']
        contato['email'] = request.form['email']
        contato['celular'] = request.form['celular']
        return redirect(url_for('contatos'))

    return render_template('atualiza.html', contato=contato)


# lesson6 routes

@app.route("/modelo-pai")
def modelo_pai():
    return render_template(
        'modelo_pai.html',
    )

@app.route("/modelo-filho")
def modelo_filho():
    return render_template(
        'modelo_filho.html',
    )

app.run(debug=True)