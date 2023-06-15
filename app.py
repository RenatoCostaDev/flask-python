from flask import Flask, render_template

contatos_list = [
    {
 	    "nome" : "flask",
        "email" : "flask@email.com",
        "celular" : "00000000",
        "tags" : ["Flask", "Flask_2"], #lista 
        'links_img_tag' : ['https://flask.palletsprojects.com/en/2.3.x/'] #lista
    },
    {
 	    "nome" : "python",
        "email" : "python@email.com",
        "celular" : "00000000",
        "tags" : ["Python", "Python_2"], #lista 
        'links_img_tag' : ['https://www.python.org/'] #lista
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

@app.route("/adicionar-contato")
def contatos_form():
    return render_template(
        'cadastro.html',
    )

app.run(debug=True)