from flask import Flask, render_template

links = [
    {'nome': 'linkedin', 'url': 'https://www.linkedin.com/in/renatocostadev/'},
    {'nome': 'gitHub', 'url': 'https://github.com/RenatoCostaDev'},
]

'''
Crie uma lista com 20 usuários (nome, idade) no python e, em seguida,
 renderize uma tabela no HTML usando os laços do jinja2.
'''
usuarios = [("João", 25), 
            ("Maria", 35), 
            ("Pedro", 19), 
            ("Ana", 28), 
            ("Rafael", 31),
            ("Juliana", 22),
            ("Lucas", 27),
            ("Lívia", 24),
            ("Renato", 29),
            ("Mariana", 30),
            ("Caio", 23),
            ("Laura", 26),
            ("Gustavo", 21),
            ("Aline", 33),
            ("Fernando", 38),
            ("Carla", 47),
            ("Vinícius", 36),
            ("Daniela", 42),
            ("Marcelo", 40),
            ("Bianca", 20)
]

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template(
         'index.html',
         links=links,
         usuarios=usuarios,
         media_idades=media_idades,
         lista_carros=lista_carros
    )

'''
Na lista criada na atividade anterior,
 faça uma condicional para exibir (em uma table do HTML) apenas os usuários cuja idade é maior
  ou igual à média (calculada a partir da lista criada).
'''
def calc_media(interavel):
    soma_idades = 0
    for usuario in usuarios:
        soma_idades += usuario[1]
    return soma_idades / len(usuarios)

media_idades = calc_media(usuarios)

'''
Crie uma classe chamada Car. Ela deve incluir atributos de nome, marca, modelo e cor.
 Em seguida, inclua três desses objetos em uma lista.
 Mostre em uma tabela no HTML os carros criados no python 
 e adicione uma forma (um quadrado) com a cor do veículo.  
'''
class Car:
    def __init__(self, nome, marca, modelo, cor):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

carro1 = Car("Fusca", "Volkswagen", "75", "Red")
carro2 = Car("Gol", "Volkswagen", "2010", "Black")
carro3 = Car("Onix", "Chevrolet", "2021", "Blue")

lista_carros = [carro1, carro2, carro3]


app.run(debug=True)
