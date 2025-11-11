import platform
import psutil
import os
import json

# @app.route = 
# # Obtém versão do S.O. subjacente
# print(platform.platform())

# # Obtém PID
# print(os.getpid())

# #Obtém uso de CPU em porcentagem
# print(psutil.cpu_percent())

# # Obtém uso de memória em MB
# print(psutil.vitual_memory().used // 1024 ** 2)

print("Nome: Brenda Barbosa")
metricas = {
    'so' : platform.platform(),
    'pid' : os.getpid(),
    'uso_cpu' : psutil.cpu_percent(),
    'memoria_mb': psutil.virtual_memory().used // 1024 ** 2
}

# transforma resultados em texto e ignora ascii
print(json.dumps(metricas, ensure_ascii=False))