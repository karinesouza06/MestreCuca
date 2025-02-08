from flask import Flask, render_template, redirect, url_for
from database.db import init_db
from controllers.user_controller import user_bp, login_manager
from controllers.recipe_controller import recipe_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'muitodificil'

login_manager.init_app(app)

# Registrar blueprints
app.register_blueprint(user_bp)
app.register_blueprint(recipe_bp)

def initialize_database():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)