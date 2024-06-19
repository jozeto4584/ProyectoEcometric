import random

def generadorDatosRuido () :

    lisDatosRuido = []
    for i in range (200):
        comuna=random.choice(['comunaNororientalk1', 'ComunaOriental3', 'Comunacentral10','comunaOccidental8', 'ComunaOccidental9'])
        nombre= random.choice(['facundo Benites','Ana Sanchez','Rosalba Oz','Maria rincon','Karla giraldo'])
        dBdiurnos=random.randint(100,140)
        dBnocturnos=random.randint(20,60)
        fecha=random.choice(['2024-04-15','2024-04-16','2024-04-17','2024-04-17','sin'])
        
        
     

        encuesta=[comuna,nombre,dBdiurnos,dBnocturnos,fecha]

        lisDatosRuido.append(encuesta)

    return lisDatosRuido

print(generadorDatosRuido()) 
    





