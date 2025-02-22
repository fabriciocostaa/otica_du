from flask_restful import Resource, reqparse
from models.clientes import PacienteModel
import sqlite3
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, jwt_required
from functools import wraps
from flask import request

def token_to_header_middleware(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get("token_de_acesso")

        if token:
            request.headers = {**request.headers, "Authorization": f"Bearer {token}"}
        return f(*args, **kwargs)
    
    return decorated_function


class Pacientes(Resource):
    @token_to_header_middleware
    @jwt_required()
    def get(self, id):
        cliente = PacienteModel.find_cliente_by_id(id)
        if cliente == None:
            return {'message' : 'cliente not found'}, 400
        else:
            return cliente.json()
        
    @token_to_header_middleware
    @jwt_required()
    def put(self, id):
        dados = Paciente.argumentos.parse_args()

        cliente = PacienteModel.find_cliente_by_id(id)

        if dados['data_nasc']:  # Verifica se o campo data_nasc não está vazio
            dados['data_nasc'] = datetime.strptime(dados['data_nasc'], "%Y-%m-%d").date()
        else:
            dados['data_nasc'] = None  # Se estiver vazio, atribui None

        if dados['data']:  
            dados['data'] = datetime.strptime(dados['data'], "%Y-%m-%d").date()
        else:
            dados['data'] = None  

        if dados['data_ultima_consulta']:  
            dados['data_ultima_consulta'] = datetime.strptime(dados['data_ultima_consulta'], "%Y-%m-%d").date()
        else:
            dados['data_ultima_consulta'] = None  

        if cliente:
            cliente.update(**dados)
            try: 
                cliente.save()
            except:
                return {'message' : 'erro ao salvar cliente'}, 500
            
            return{'message' : 'cliente salvo com sucesso'}, 200
        
        else:
            return{'message' : 'cliente não encontrado'}, 404
         
    
    @token_to_header_middleware
    @jwt_required()
    def delete(self, id):
        cliente = PacienteModel.find_cliente_by_id(id)
        if not cliente:
            return {'message': 'Cliente não encontrado'}, 404

        user = get_jwt_identity()
        if user != "1":
            return {'message': 'Não autorizado'}, 401

        try:
            cliente.delete()
        except:
            return {'message': 'Erro ao deletar cliente'}, 500

        return {'message': 'Cliente deletado com sucesso'}, 200
        

class Paciente(Resource):
    # Definir os parâmetros esperados
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="O campo 'nome' é obrigatório.")
    argumentos.add_argument('data', type=str)
    argumentos.add_argument('profissao', type=str)
    argumentos.add_argument('data_nasc', type=str)
    argumentos.add_argument('idade', type=str) 
    argumentos.add_argument('sexo', type=str)
    argumentos.add_argument('telefone_res', type=str)
    argumentos.add_argument('telefone_comer', type=str)
    argumentos.add_argument('telefone_cel', type=str)
    argumentos.add_argument('endereco', type=str)
    argumentos.add_argument('bairro', type=str)
    argumentos.add_argument('cidade', type=str)
    argumentos.add_argument('cep', type=str)
    argumentos.add_argument('email', type=str)
    argumentos.add_argument('data_ultima_consulta', type=str)
    argumentos.add_argument('mpc', type=str)
    argumentos.add_argument('antecedentes_pessoais', type=str)
    argumentos.add_argument('antecedentes_familiares', type=str)
    argumentos.add_argument('medicamentos', type=str)
    argumentos.add_argument('formato_pupila', type=str)
    argumentos.add_argument('rebordo_pupila', type=str)
    argumentos.add_argument('diametro_pupila', type=str)
    argumentos.add_argument('reacao_luz', type=str)
    argumentos.add_argument('reacao_consensual', type=str)
    argumentos.add_argument('reacao_acomodativa', type=str)
    argumentos.add_argument('fixacao', type=str)
    argumentos.add_argument('dominancia', type=str)
    argumentos.add_argument('hirshberg', type=str)
    argumentos.add_argument('brucner', type=str)
    argumentos.add_argument('angulo_kappa_od', type=str)
    argumentos.add_argument('angulo_kappa_oe', type=str)
    argumentos.add_argument('receituario', type=str)
    argumentos.add_argument('observacoes', type=str)

    @token_to_header_middleware
    @jwt_required()
    def get(self):
        connection = sqlite3.connect("instance/banco.db")
        cursor = connection.cursor()

        consulta = "SELECT * FROM pacientes"

        resultado = cursor.execute(consulta)

        pacientes = []

        for linha in resultado:
            pacientes.append({
                'id_cliente' : linha[0],
                'nome': linha[1],
                'data_nasc': linha[4],
                'sexo': linha[6],
                'telefone_res' : linha[7],
                'profissao' : linha[3],
                'idade' : linha[5]
            })

        return {"message" : pacientes}
    
    @token_to_header_middleware
    @jwt_required()
    def post(self):
        dados = Paciente.argumentos.parse_args()
    
        if dados['data_nasc']:  # Verifica se o campo data_nasc não está vazio
            dados['data_nasc'] = datetime.strptime(dados['data_nasc'], "%Y-%m-%d").date()
        else:
            dados['data_nasc'] = None  # Se estiver vazio, atribui None

        if dados['data']:  
            dados['data'] = datetime.strptime(dados['data'], "%Y-%m-%d").date()
        else:
            dados['data'] = None  

        if dados['data_ultima_consulta']:  
            dados['data_ultima_consulta'] = datetime.strptime(dados['data_ultima_consulta'], "%Y-%m-%d").date()
        else:
            dados['data_ultima_consulta'] = None  
        
        # Criar o objeto paciente
        try:
            objeto_paciente = PacienteModel(**dados)
            objeto_paciente.save()
        except Exception as e:
            return {'message': f'Erro ao salvar paciente: {str(e)}'}, 500

        return {'message': 'Paciente salvo com sucesso'}, 200