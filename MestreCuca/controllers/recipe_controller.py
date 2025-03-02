from flask import Blueprint, request, render_template, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from models.recipe import Receita
from models.user import User, current_user
from database.db import db_session

recipe_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipe_bp.route('/', methods=['GET', 'POST'])
def cadastrar_receitas():
    if request.method == 'POST':
        nome_user = request.form['nome_user']
        nome_receita = request.form['nome_receita']
        categoria = request.form['categoria']
        ingredientes = request.form['ingredientes']
        modo_preparo = request.form['modo_preparo']

        if Receita.exists(nome_receita):
            flash("Receita já cadastrada.")
        else:
            user_id = User.get_id_by_name(nome_user)  
            if user_id is None:
                flash("Usuário não encontrado.")
                return redirect(url_for('recipes.cadastrar_receitas'))

            receita = Receita(nome_receita=nome_receita, nome_user=nome_user, categoria=categoria, ingredientes=ingredientes, modo_preparo=modo_preparo)
            db_session.add(receita)
            db_session.commit()
            return render_template('cadastrar_receitas.html', user=current_user)
    return render_template('cadastrar_receitas.html', user=current_user)

@recipe_bp.route('/pagina_receitas', methods=['GET'])
def pagina_receitas():
    receitas = Receita.get_receitas()
    return render_template('pagina_receitas.html', receitas=receitas)

@recipe_bp.route('/editar_receita', methods=['GET', 'POST'])
def editar_receita():
    if request.method == 'POST':
        nome_user = request.form['nome_user']
        nome_receita = request.form['nome_receita']
        categoria = request.form['categoria']
        ingredientes = request.form['ingredientes']
        modo_preparo = request.form['modo_preparo']
        
        Receita.update(nome_user, nome_receita, categoria, ingredientes, modo_preparo)
        return redirect(url_for('recepies.pagina_receitas'))
        
@recipe_bp.route('/excluir_receita/<int:id>', methods=['GET'])
def excluir_receitas(id):   
       Receita.delete(id)
       return redirect(url_for('recepies.pagina_receitas'))


    
   
    
