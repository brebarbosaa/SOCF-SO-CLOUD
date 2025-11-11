from flask import Flask
import platform
import psutil
import os
import json

app = Flask(__name__) 

@app.route('/')
def home():
    return """
    <h1>SO em Cloud</h1>
    <p>Digite '/metricas' ou '/info' na url para mais informações!</p> 
    """

@app.route('/info')
def info():
    return "Aluna: Brenda Gabrielli Barbosa"

@app.route('/metricas')
def exibe_metricas():
    metricas = {
        'Sistema Operacional:' : platform.platform(),
        'PID:' : os.getpid(),
        'Uso de CPU:' : psutil.cpu_percent(),
        'Memoria utilizada:': psutil.virtual_memory().used // 1024 ** 2
    }  
    # transforma resultados em texto e ignora ascii
    return json.dumps(metricas, ensure_ascii=False)

APP = app

if __name__ == '__main__':
    app.run(debug=True)