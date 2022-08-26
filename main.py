from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste.sqlite3'

db = SQLAlchemy(app)

####################################################

class Funcionarios(db.Model):
    id_funcionario = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__ (self):
        return str(self.id_funcionario) + " " +  str(self.name) + " " + str(self.email)

class Clientes(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return str(self.name) + " " + str(self.email)

class Equipamentos(db.Model):
    id_equipamento = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    codigo = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return str(self.name) + " " + str(self.codigo)

####################################################

def create_funcionario(name, email):

    #admin = User(username='Adalto', email='adalto@example.com')
    #guest = User(username='João', email='joao@example.com')

    teste = Funcionarios(name=name, email=email)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

def create_cliente(name, email):
    teste = Clientes(name=name, email=email)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

def create_equipamento(name, codigo):
    teste = Equipamentos(name=name, codigo=codigo)

    db.session.add(teste)
    db.session.commit()
    db.session.close()

def delete_cliente(id):
    Clientes.query.filter(Clientes.id_cliente == f'{id}').delete()
    db.session.commit()
    db.session.close()

def delete_funcionario(id):
    Funcionarios.query.filter(Funcionarios.id_funcionario == f'{id}').delete()
    db.session.commit()
    db.session.close()

def delete_equipamento(id):
    Equipamentos.query.filter(Equipamentos.id_equipamento == f'{id}').delete()
    db.session.commit()
    db.session.close()

####################################################

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/funcionarios', methods=["GET", "POST"])
@app.route('/funcionarios')
def funcionarios():
    if request.method == 'POST':
        name = request.form.get("nome")
        email = request.form.get("email")
        create_funcionario(name=name, email=email)
    return render_template('funcionarios.html')

@app.route('/clientes', methods=["GET", "POST"])
@app.route('/clientes')
def clientes():
    if request.method == 'POST':
        name = request.form.get("nome")
        email = request.form.get("email")
        create_cliente(name=name, email=email)
    return render_template('clientes.html')

@app.route('/equipamentos', methods=["GET", "POST"])
@app.route('/equipamentos')
def equipamentos():
    if request.method == 'POST':
        name = request.form.get("nome")
        codigo = request.form.get("codigo")
        create_equipamento(name=name, codigo=codigo)
    return render_template('equipamentos.html')

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
@app.route('/deleteclientes')
def deletar_clientes():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_cliente(id)
    return render_template('deleteclientes.html')


@app.route('/deletefuncionarios', methods=["GET", "POST"])
@app.route('/deletefuncionarios')
def deletar_funcionarios():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_funcionario(id)
    return render_template('deletefuncionarios.html')

@app.route('/deleteequipamento', methods=["GET", "POST"])
@app.route('/deleteequipamento')
def deletar_equipamentos():
    if request.method == 'POST':
        id = request.form.get("id")
        delete_equipamento(id)
    return render_template('deleteequipamentos.html')

####################################################

if __name__ =="__main__":
	db.create_all()
	app.run(debug=True, use_reloader=False)
