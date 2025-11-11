from flask import Flask
import platform
import psutil
import os
import json

app = Flask(__name__)

metricas = {
    'so' : platform.platform(),
    'pid' : os.getpid(),
    'uso_cpu' : psutil.cpu_percent(),
    'memoria_mb': psutil.virtual_memory().used // 1024 ** 2
    }   

@app.route('/info')
def info():
    return "Brenda Gabrielli Barbosa"

@app.route('/metricas')
def metricas():
    # transforma resultados em texto e ignora ascii
    return json.dumps(metricas, ensure_ascii=False)

APP = app

if __name__ == '__main__':
    app.run(debug=True)