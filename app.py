from flask import Flask, render_template, request, redirect

contatos_list = [
    {
 	    "nome" : "flask",
        "email" : "flask@email.com",
        "celular" : "00000000",
    },
    {
 	    "nome" : "python",
        "email" : "python@email.com",
        "celular" : "00000000",
    },
]


app = Flask(__name__)

@app.route("/contatos")
def contatos():
    return render_template(
        'contatos.html',
        contatos_list=contatos_list,
        zip=zip,
    )

#  obs: zip is a Python function as such
#  you will need to pass the same way you pass
#  other variables to be used in your jinja template.

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
    # email_recebido = request.form['email']
    for i in range(len(contatos_list)):
        if contatos_list[i]['email'] == str(email): #Verifica o email recebido
            contatos_list.pop(i)
        return redirect('/contatos')
    app.run()


app.run(debug=True)