from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vinicius:123456@127.0.0.1/transcolar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DataTranscolar(db.Model):
    __tablename__ = 'data_transcolar'
    anobase = db.Column(db.Integer)
    sre = db.Column(db.String(200))
    sigla_tipo_ensino = db.Column(db.String(200))  # Adicione esta coluna
    inep_escola = db.Column(db.String(8), primary_key=True)  # Definido como parte da chave primária
    nome_escola = db.Column(db.String(200))
    nome_aluno = db.Column(db.String(200), primary_key=True)  # Definido como parte da chave primária
    tipo_dependencia = db.Column(db.String(200))  # Adicione esta coluna

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    data = db.session.query(
        DataTranscolar.sre,
        DataTranscolar.nome_aluno,
        DataTranscolar.sigla_tipo_ensino,
        DataTranscolar.inep_escola,
        DataTranscolar.nome_escola,
        DataTranscolar.tipo_dependencia
    ).all()
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
