import random

def generadorDatosReciclaje():

    listaReciclaje=[]
    for i in range(200):
        barrio=random.choice(["Prados", "La inmaculada", "trapiche", "la doctora", "holanda"])
        tipoReciclaje=random.choice(["carton","plastico","vidrios","metales"])
        tiempoSemana=random.randint(1,4)
        nombre=random.choice(["melisa agudelo","cristian narvaez","jhon agustin","claudia mora","carlos delgado"])
        fecha=random.choice(['2024-03-12','2024-03-15','2024-04-10','2024-04-15','sin'])
        
        


        encuesta=[barrio,tipoReciclaje,tiempoSemana,nombre,fecha]

        listaReciclaje.append(encuesta)
    
    return listaReciclaje

print(generadorDatosReciclaje())




















#Reciclaje
""" barrio
tiporeciclaje
tiempo
nombre
fecha
 """
