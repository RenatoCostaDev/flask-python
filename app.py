from flask import Flask,render_template

contatos = [
    {
 	    "nome" : "fulano",
        "email" : "fulano@email.com",
        "celular" : "00000000",
        "tags" : ["trabalho"], #lista 
        'links_img_tag' : ['https://…..png'] #lista
    }
]

app = Flask(__name__)

@app.route("/contatos")
def contatos():
    return render_template(
        'contatos.html',
        contatos=contatos
    )

app.run(debug=True)
