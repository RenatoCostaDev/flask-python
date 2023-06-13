from flask import Flask, render_template

links = [
    {'nome': 'linkedin', 'url': 'https://www.linkedin.com/in/renatocostadev/'},
    {'nome': 'gitHub', 'url': 'https://github.com/RenatoCostaDev'},
]

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template(
         'index.html',
         links=links
    )

app.run(debug=True)
