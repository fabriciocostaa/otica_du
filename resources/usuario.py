from flask_restful import reqparse, Resource
from datetime import timedelta
from models.usuario import UserModel
import hmac
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from flask import make_response, jsonify
from blacklist import BLACKLIST
from resources.clientes import token_to_header_middleware

atributos = reqparse.RequestParser()
atributos.add_argument('login', type = str, required = True, help = "The field 'login' cannot be left blank")
atributos.add_argument('senha', type = str, required = True, help = "The field 'senha' cannot be left blank")
 
# class UserRegister(Resource):
#     def post(self):
#         dados = atributos.parse_args()

#         try:
#             user_object = UserModel(**dados)
#             user_object.save()
#         except:
#             return{"message" : "Erro interno"}, 500
        
#         return{"message" : "usuário criado com sucesso"}, 201
    
class UserLogin(Resource):
    @classmethod
    def post(cls):
        dados = atributos.parse_args()

        user = UserModel.find_by_login(dados['login'])

        if user and hmac.compare_digest(user.senha, dados['senha']):
            expires = timedelta(hours= 3)
            token_de_acesso = create_access_token(identity=str(user.user_id), expires_delta=expires)
            response = make_response(jsonify({"message": "Login realizado com sucesso"}))
            response.set_cookie('token_de_acesso', token_de_acesso, httponly=True)
            return response
        return {'message' : 'login e senha incorretos'}, 400
    
class UserLogout(Resource):
    @token_to_header_middleware
    @jwt_required()
    def post(self):
        try:
            jwt_data = get_jwt()

            jwt_id = jwt_data.get('jti', None)
            
            if jwt_id is None:
                return {"message" : "invalid token"}, 400
            
            BLACKLIST.add(jwt_id)
            return {"message" : "você foi deslogado"}, 200
        
        except:
            return {"message" : "ocorreu algum erro durante o processo"}, 500