from flask import Blueprint, request, render_template, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User, current_user
from database.db import db_session

from flask_login import LoginManager, login_user, login_required, logout_user
login_manager = LoginManager()

user_bp = Blueprint('users', __name__, url_prefix='/users')

@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(user_id) 

@user_bp.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        user = db_session.query(User).filter_by(nome=nome).first()  

        if user and check_password_hash(user.senha, senha): 
            login_user(user)
            flash("Você está logado")
            return render_template("cadastrar_receitas.html", user=user)
            #return redirect(url_for('recipes.cadastrar_receitas'))
        else:
            flash("Dados incorretos")
            return redirect(url_for('users.login')) 
    return render_template('login.html')


@user_bp.route('/', methods=['GET', 'POST'])
def cadastrar_user():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        confirma_senha = request.form['confirmarSenha']

        if User.exists(email):
            flash("Email já cadastrado.")
        elif User.exists_by_name(nome):
            flash("Já existe um usuário com esse nome.")
        else:
            if senha == confirma_senha:
                user = User(nome=nome, email=email, senha=generate_password_hash(senha))
                db_session.add(user)
                db_session.commit()
                login_user(user)
                flash("Cadastro realizado com sucesso")
                return redirect(url_for('users.login'))
            else:
                flash("As senhas não conferem.")

    return render_template("cadastrar_usuarios.html")

@user_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Você foi desconectado.")
    return redirect(url_for('index'))

