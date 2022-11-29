from flask import Flask, render_template

def create_app() -> Flask:
    """Fabrica de Aplicação Flask"""
    app = Flask(__name__)

    return app

app = create_app()

@app.route('/')
def index():
    return render_template('base.html')
