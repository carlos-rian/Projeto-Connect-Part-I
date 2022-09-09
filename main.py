from flask import Flask, render_template, request, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.sqlite3'

db = SQLAlchemy(app)

class Funcionarios(db.Model):
    id_funcionario = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    senha = db.Column(db.String(12), nullable=False)

    def create_funcionario(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()
    
    def atualizar_funcionarios(id, nome, email):
        funcionario = Funcionarios.query.filter_by(id_funcionario=f'{id}').first()
        funcionario.email = email
        funcionario.name = nome
        db.session.commit()
        db.session.close()

    def delete_funcionario(id):
        Funcionarios.query.filter(Funcionarios.id_funcionario == f'{id}').delete()
        db.session.commit()
        db.session.close()

class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def create_cliente(name, email):
        cliente = Clientes(name=name, email=email)

        db.session.add(cliente)
        db.session.commit()
        db.session.close()

    def atualizar_clientes(id, nome, email):
        cliente = Clientes.query.filter_by(id_cliente=f'{id}').first()
        cliente.email = email
        cliente.name = nome
        db.session.commit()
        db.session.close()

    def delete_cliente(id):
        Clientes.query.filter(Clientes.id_cliente == f'{id}').delete()
        db.session.commit()
        db.session.close()


class Equipamentos(db.Model):
    id_equipamento = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    codigo = db.Column(db.Integer, nullable=False)
    qtde = db.Column(db.Integer, nullable=False)

    def create_equipamento(name, codigo, qtde):
        equipamento = Equipamentos(name=name, codigo=codigo, qtde=qtde)

        db.session.add(equipamento)
        db.session.commit()
        db.session.close()

    def delete_equipamento(id):
        Equipamentos.query.filter(Equipamentos.id_equipamento == f'{id}').delete()
        db.session.commit()
        db.session.close()

    def atualizar_equipamentos(id, nome, codigo, qtde):
        equipamento = Equipamentos.query.filter_by(id_equipamento=f'{id}').first()
        equipamento.codigo = codigo
        equipamento.name = nome
        equipamento.qtde = qtde
        db.session.commit()
        db.session.close()


@app.route('/')
def main():
    return render_template('index.html')

# ok
@app.route('/cadastrarfuncionarios')
def get_funcionarios():
    return render_template('cadastrarfuncionarios.html')

# ok
@app.route('/cadastrarfuncionarios', methods=["POST"])
def cadastrar_funcionarios():
    name = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    # class instance 
    db = Funcionarios(name=name, email=email, senha=senha)
    # crio o registro no banco
    db.create_funcionario()
    # busco todos os registros
    funcionarios = db.query.all()
    return render_template('consultafuncionarios.html', funcionarios=funcionarios)

# ok
@app.route('/cadastrarclientes')
def get_clientes():
    return render_template('cadastrarclientes.html')

# ok
@app.route('/cadastrarclientes', methods=["POST"])
def cadastrar_clientes():
    name = request.form.get("nome")
    email = request.form.get("email")
    Clientes.create_cliente(name=name, email=email)
    clientes = Clientes.query.all()
    return render_template('consultaclientes.html', clientes=clientes)

@app.route('/cadastrarequipamentos')
def get_equipamentos():
    return render_template('cadastrarequipamentos.html')

@app.route('/cadastrarequipamentos', methods=["POST"])
def cadastrar_equipamentos():
    name = request.form.get("nome")
    codigo = request.form.get("codigo")
    qtde = request.form.get("qtde")
    Equipamentos.create_equipamento(name=name, codigo=codigo, qtde=qtde)
    equipamentos = Equipamentos.query.all()
    return render_template('consultaequipamentos.html', equipamentos=equipamentos)

@app.route('/consultaequipamentos')
def consulta_equipamentos():
    equipamentos = Equipamentos.query.all()
    return render_template('consultaequipamentos.html', equipamentos=equipamentos)

@app.route('/consultafuncionarios')
def consulta_funcionarios():
    funcionarios = Funcionarios.query.all()
    return render_template('consultafuncionarios.html', funcionarios=funcionarios)

@app.route('/consultaclientes')
def consulta_clientes():
    clientes = Clientes.query.all()
    return render_template('consultaclientes.html', clientes=clientes)

@app.route('/deleteclientes')
def get_deletar_clientes():
    return render_template('deleteclientes.html')

@app.route('/deleteclientes', methods=["POST"])
def deletar_clientes():
    id = request.form.get("id")
    Clientes.delete_cliente(id)
    clientes = Clientes.query.all()
    return render_template('consultaclientes.html', clientes=clientes)

@app.route('/deletefuncionarios')
def get_deletar_funcionarios():
    return render_template('deletefuncionarios.html')

@app.route('/deletefuncionarios', methods=["POST"])
def deletar_funcionarios():
    id = request.form.get("id")
    Funcionarios.delete_funcionario(id)
    funcionarios = Funcionarios.query.all()
    return render_template('consultafuncionarios.html', funcionarios=funcionarios)

@app.route('/deleteequipamento')
def get_deletar_equipamentos():
    return render_template('deleteequipamentos.html')

@app.route('/deleteequipamento', methods=["POST"])
def deletar_equipamentos():
    id = request.form.get("id")
    Equipamentos.delete_equipamento(id)
    equipamentos = Equipamentos.query.all()
    return render_template('consultaequipamentos.html', equipamentos=equipamentos)


@app.route('/atualizarclientes')
def get_atualizar_cliente():
    return render_template('atualizarclientes.html')

@app.route('/atualizarclientes', methods=["POST"])
def atualizar_cliente():
    id = request.form.get("id")
    nome = request.form.get("nome")
    email = request.form.get("email")
    Clientes.atualizar_clientes(id, nome, email)
    clientes = Clientes.query.all()
    return render_template('consultaclientes.html', clientes=clientes)

@app.route('/atualizarequipamentos')
def get_atualizar_equipamento():
    return render_template('atualizarequipamentos.html')

@app.route('/atualizarequipamentos', methods=["GET", "POST"])
def atualizar_equipamento():
    id = request.form.get("id")
    nome = request.form.get("nome")
    codigo = request.form.get("codigo") 
    qtde = request.form.get("qtde")
    Equipamentos.atualizar_equipamentos(id, nome, codigo, qtde)
    equipamentos = Equipamentos.query.all()
    return render_template('consultaequipamentos.html', equipamentos=equipamentos)

@app.route('/atualizarfuncionarios')
def get_atualizar_funcionario():
    return render_template('atualizarfuncionarios.html')

@app.route('/atualizarfuncionarios', methods=["GET", "POST"])
def atualizar_funcionario():
    id = request.form.get("id")
    nome = request.form.get("nome")
    email = request.form.get("email")
    Funcionarios.atualizar_funcionarios(id, nome, email)
    funcionarios = Funcionarios.query.all()
    return render_template('consultafuncionarios.html', funcionarios=funcionarios)

if __name__ =="__main__":
	db.create_all()
	app.run(debug=True)
