from flask import Flask
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def rota_home():
    return {"data": "Hello Flask!"}

@app.route('/current_datetime')
def rota_current_datetime():
    data_atual = datetime.now()
    data_atual_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S %p")
    hora_atual = datetime.now().hour
    msg = ''

    if (hora_atual < 12):
        msg += 'Bom dia!'
    elif (12 <= hora_atual < 18):
        msg += 'Boa tarde!'
    else:
        msg += 'Boa noite!'
    
    return {"current_datetime": data_atual_formatada, "message": msg}