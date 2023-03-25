from flask import Blueprint, jsonify, redirect, request, render_template
from database.classes import Grupo, Usuario


admin_bp = Blueprint( 'admin', __name__, template_folder='templates')


@admin_bp.route("/")
def home():
    return render_template("admin/home.html")


@admin_bp.route("/Operacoes")
def oper():
    return render_template("admin/oper_0_menu.html")


@admin_bp.route("/Operacoes/RoscaInterna")
def oper_rosca_int():
    return render_template("admin/oper_5_thread_mill.html")


@admin_bp.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        form = request.form
        print(f'''
        ++++ MENSAGEM ENVIADA ++++
        -> Nome: {form.get('nome')}
        -> E-mail: {form.get('email')}
        -> Assunto: {form.get('assunto')}
        -> Como Conheceu: {form.get('conheceu')}
        -> Mensagem:
        {form.get('mensagem')}
        ''')

    return render_template('contato.html')





