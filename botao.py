from flask import Flask, render_template
from CRUD import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/mostrar", methods=["POST"])
def mostra():
    return render_template("index.html",msg=b)

app.run(debug=True)