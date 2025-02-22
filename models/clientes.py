from sql_alchemy import banco

#ORM - pesquisar !

class PacienteModel(banco.Model):
    __tablename__ = 'pacientes'

    id = banco.Column(banco.Integer, primary_key=True, autoincrement=True) # ID único para cada paciente
    nome = banco.Column(banco.String(80), nullable=False)  # Nome do paciente
    data = banco.Column(banco.Date(), nullable=True)  # Data
    profissao = banco.Column(banco.String(100), nullable=True)  # Profissão
    data_nasc = banco.Column(banco.Date(), nullable=True)  # Data de nascimento
    idade = banco.Column(banco.String(3), nullable=True)  # Idade
    sexo = banco.Column(banco.String(1), nullable=True)  # Sexo (M ou F)
    telefone_res = banco.Column(banco.String(20), nullable=True)  # Telefone residencial
    telefone_comer = banco.Column(banco.String(20), nullable=True)  # Telefone comercial
    telefone_cel = banco.Column(banco.String(20), nullable=True)  # Telefone celular
    endereco = banco.Column(banco.String(200), nullable=True)  # Endereço
    bairro = banco.Column(banco.String(100), nullable=True)  # Bairro
    cidade = banco.Column(banco.String(100), nullable=True)  # Cidade
    cep = banco.Column(banco.String(10), nullable=True)  # CEP
    email = banco.Column(banco.String(100), nullable=True)  # Email
    data_ultima_consulta = banco.Column(banco.Date(), nullable=True)  # Data da última consulta
    mpc = banco.Column(banco.Text, nullable=True)  # M.P.C
    antecedentes_pessoais = banco.Column(banco.Text, nullable=True)  # Antecedentes pessoais
    antecedentes_familiares = banco.Column(banco.Text, nullable=True)  # Antecedentes familiares
    medicamentos = banco.Column(banco.Text, nullable=True)  # Medicamentos em uso
    formato_pupila = banco.Column(banco.String(50), nullable=True)  # Formato da pupila
    rebordo_pupila = banco.Column(banco.String(50), nullable=True)  # Rebordo da pupila
    diametro_pupila = banco.Column(banco.String(50), nullable=True)  # Diâmetro da pupila
    reacao_luz = banco.Column(banco.String(50), nullable=True)  # Reação à luz
    reacao_consensual = banco.Column(banco.String(50), nullable=True)  # Reação consensual
    reacao_acomodativa = banco.Column(banco.String(50), nullable=True)  # Reação acomodativa
    fixacao = banco.Column(banco.String(50), nullable=True)  # Fixação
    dominancia = banco.Column(banco.String(50), nullable=True)  # Dominância
    hirshberg = banco.Column(banco.String(50), nullable=True)  # Hirshberg
    brucner = banco.Column(banco.String(50), nullable=True)  # Brucner
    angulo_kappa_od = banco.Column(banco.String(50), nullable=True)  # Ângulo Kappa OD
    angulo_kappa_oe = banco.Column(banco.String(50), nullable=True)  # Ângulo Kappa OE
    receituario = banco.Column(banco.String(200), nullable=True)
    observacoes = banco.Column(banco.String(200), nullable=True) 

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def json(self):
        # Converte objetos date para strings
        def format_date(value):
            return value.isoformat() if value else None

        return {
            "id": self.id,
            "nome": self.nome,
            "data": format_date(self.data),
            "profissao": self.profissao,
            "data_nasc": format_date(self.data_nasc),
            "idade": self.idade,
            "sexo": self.sexo,
            "telefone_res": self.telefone_res,
            "telefone_comer": self.telefone_comer,
            "telefone_cel": self.telefone_cel,
            "endereco": self.endereco,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "cep": self.cep,
            "email": self.email,
            "data_ultima_consulta": format_date(self.data_ultima_consulta),
            "mpc": self.mpc,
            "antecedentes_pessoais": self.antecedentes_pessoais,
            "antecedentes_familiares": self.antecedentes_familiares,
            "medicamentos": self.medicamentos,
            "formato_pupila": self.formato_pupila,
            "rebordo_pupila": self.rebordo_pupila,
            "diametro_pupila": self.diametro_pupila,
            "reacao_luz": self.reacao_luz,
            "reacao_consensual": self.reacao_consensual,
            "reacao_acomodativa": self.reacao_acomodativa,
            "fixacao": self.fixacao,
            "dominancia": self.dominancia,
            "hirshberg": self.hirshberg,
            "brucner": self.brucner,
            "angulo_kappa_od": self.angulo_kappa_od,
            "angulo_kappa_oe": self.angulo_kappa_oe,
            "receituario": self.receituario,
            "observacoes": self.observacoes
        }
    
    @classmethod
    def find_cliente_by_id(cls, id):
       cliente = cls.query.filter_by(id = id).first()
       if cliente:
           return cliente
       return None 

    def save(self):
        banco.session.add(self)
        banco.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()
