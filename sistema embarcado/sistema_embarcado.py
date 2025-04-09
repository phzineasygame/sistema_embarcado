import time
import random


def sensor_estufa():
    
    temperatura = random.uniform(15, 35)
    umidade = random.uniform(40, 90)
    return temperatura, umidade


def controle_equipamentos(temperatura):
    if temperatura > 29:
        print("Ar condicionado ligado")
    else:
        print("Ar condicionado desligado")

    if temperatura < 17:
        print("Aquecedor ligado")
    else:
        print("Aquecedor desligado")


def detector_umidade(umidade):
    if umidade > 40:
        print("A qualidade do ar está boa!")
    else:
        print("A qualidade do ar está ruim...")


def monitorar():
    while True:
        
        temperatura, umidade = sensor_estufa()
        
        controle_equipamentos(temperatura)
        detector_umidade(umidade)
        
        print()
        print()    
        
        time.sleep(5)


monitorar()
