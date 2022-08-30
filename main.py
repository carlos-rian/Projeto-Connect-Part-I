from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.sqlite3'

db = SQLAlchemy(app)

####################################################

# criando o banco de dados dos Funcionários
class Funcionarios(db.Model):
    id_funcionario = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__ (self):
        return str(self.id_funcionario) + " " +  str(self.name) + " " + str(self.email)

# criando o banco de dados dos Clientes
class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return str(self.name) + " " + str(self.email)

# criando o banco de dados dos Equipamentos
class Equipamentos(db.Model):
    id_equipamento = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    codigo = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return str(self.name) + " " + str(self.codigo)

####################################################

# função responsável pela criação dos funcionários
def create_funcionario(name, email):

    teste = Funcionarios(name=name, email=email)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

# função responsável pela criação dos clientes
def create_cliente(name, email):
    teste = Clientes(name=name, email=email)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

# função responsável pela criação dos equipamentos
def create_equipamento(name, codigo):
    teste = Equipamentos(name=name, codigo=codigo)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

# função responsável por deletar os clientes
def delete_cliente(id):
    Clientes.query.filter(Clientes.id_cliente == f'{id}').delete()
    db.session.commit()
    db.session.close()

# função responsável por deletar os funcionários
def delete_funcionario(id):
    Funcionarios.query.filter(Funcionarios.id_funcionario == f'{id}').delete()
    db.session.commit()
    db.session.close()

# função responsável por deletar os equipamentos
def delete_equipamento(id):
    Equipamentos.query.filter(Equipamentos.id_equipamento == f'{id}').delete()
    db.session.commit()
    db.session.close()

####################################################

def atualizar_clientes(id, nome, email):
    cliente = Clientes.query.filter_by(id_cliente=f'{id}').first()
    cliente.email = email
    cliente.name = nome
    db.session.commit()
    db.session.close()

def atualizar_equipamentos(id, nome, codigo):
    equipamento = Equipamentos.query.filter_by(id_equipamento=f'{id}').first()
    equipamento.codigo = codigo
    equipamento.name = nome
    db.session.commit()
    db.session.close()

def atualizar_funcionarios(id, nome, email):
    funcionario = Funcionarios.query.filter_by(id_funcionario=f'{id}').first()
    funcionario.email = email
    funcionario.name = nome
    db.session.commit()
    db.session.close()

####################################################

#rota para a página inicial
@app.route('/')
def main():
    return render_template('index.html')

#rota para a página de cadastro dos funcionários
@app.route('/cadastrarfuncionarios', methods=["GET", "POST"])
def cadastrar_funcionarios():
    if request.method == 'POST':
        name = request.form.get("nome")
        email = request.form.get("email")
        create_funcionario(name=name, email=email)
    return render_template('cadastrarfuncionarios.html')

#rota para a página de cadastro dos clientes
@app.route('/cadastrarclientes', methods=["GET", "POST"])
def cadastrar_clientes():
    if request.method == 'POST':
        name = request.form.get("nome")
        email = request.form.get("email")
        create_cliente(name=name, email=email)
    return render_template('cadastrarclientes.html')

#rota para a página de cadastro dos equipamentos
@app.route('/cadastrarequipamentos', methods=["GET", "POST"])
def cadastrar_equipamentos():
    if request.method == 'POST':
        name = request.form.get("nome")
        codigo = request.form.get("codigo")
        create_equipamento(name=name, codigo=codigo)
    return render_template('cadastrarequipamentos.html')

####################################################

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


####################################################


@app.route('/deleteclientes', methods=["GET", "POST"])
def deletar_clientes():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_cliente(id)
    return render_template('deleteclientes.html')

@app.route('/deletefuncionarios', methods=["GET", "POST"])
def deletar_funcionarios():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_funcionario(id)
    return render_template('deletefuncionarios.html')

@app.route('/deleteequipamento', methods=["GET", "POST"])
def deletar_equipamentos():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_equipamento(id)
    return render_template('deleteequipamentos.html')

####################################################

@app.route('/atualizarclientes', methods=["GET", "POST"])
def atualizar_cliente():
    if request.method == 'POST':
        id = request.form.get("id")
        nome = request.form.get("nome")
        email = request.form.get("email")
        atualizar_clientes(id, nome, email)
    return render_template('atualizarclientes.html')

@app.route('/atualizarequipamentos', methods=["GET", "POST"])
def atualizar_equipamento():
    if request.method == 'POST':
        id = request.form.get("id")
        nome = request.form.get("nome")
        codigo = request.form.get("codigo")
        atualizar_equipamentos(id, nome, codigo)
    return render_template('atualizarequipamentos.html')

@app.route('/atualizarfuncionarios', methods=["GET", "POST"])
def atualizar_funcionario():
    if request.method == 'POST':
        id = request.form.get("id")
        nome = request.form.get("nome")
        email = request.form.get("email")
        atualizar_funcionarios(id, nome, email)
    return render_template('atualizarfuncionarios.html')

####################################################


if __name__ =="__main__":
	db.create_all()
	app.run(debug=True, use_reloader=False)
