from flask import Flask, render_template, redirect, url_for, flash
from flask_restful import Api
from flask_jwt_extended  import JWTManager, jwt_required, get_jwt_identity
from resources.clientes import Pacientes, Paciente
from models.clientes import PacienteModel
from resources.usuario import UserLogin, UserLogout
from blacklist import BLACKLIST
import os
from dotenv import load_dotenv
from sql_alchemy import banco

load_dotenv()

app = Flask(__name__) 

app.secret_key = os.getenv("secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'cookies']
app.config['JWT_ACCESS_COOKIE_NAME'] = 'token_de_acesso'

banco.init_app(app)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(Pacientes, "/pacientes/<int:id>")
api.add_resource(Paciente, "/registrar")
api.add_resource(UserLogin, "/login_usuario")
api.add_resource(UserLogout, "/logout_usuario")

@app.before_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST 

@jwt.revoked_token_loader
def token_de_acesso_invalidado(jwt_header, jwt_payload):
    flash("você foi deslogado !")
    return redirect(url_for("home")) 

@jwt.unauthorized_loader
def token_ausente_callback(mensagem):
    flash("Você precisa estar logado! ")
    return redirect(url_for("home")) 

@app.route("/", endpoint="home")
def index():
    return render_template("login.html")

@app.route("/index", endpoint="index")
@jwt_required(locations=["cookies"])
def pagina_raiz():
    return render_template("index.html")

@app.route("/formulario")
@jwt_required(locations=["cookies"])
def formulario():
    return render_template("/formulario.html")

@app.route("/cadastrados")
@jwt_required(locations=["cookies"])
def consultar_clientes():
    return render_template("/cadastrados.html")

@app.route("/clientes/<int:id>")
@jwt_required(locations=["cookies"])
def informacao_cliente(id):
    cliente = PacienteModel.find_cliente_by_id(id)
    if cliente is None:
        return {'message': 'Cliente não encontrado'}, 404
    
    return render_template("/cliente.html")

@app.route("/editar")
@jwt_required(locations=["cookies"])
def editar_cliente():
    usuario = get_jwt_identity()
    if usuario == "1":
        return render_template("/editar_cliente.html")
    else:
        flash("Não autorizado")
        return redirect(url_for("index"))
