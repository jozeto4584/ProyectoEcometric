import random

def listaDatosArboles():

    datosSiembraArboles=[]
    for i in range (200):
        corregimiento=random.randint(1,14)
        hectareasSemabradas=random.randint(1,5)
        especieSembrada= random.choice(['Ecucalipto','cedro','fresno','Bambu','sauce'])
        nombres=random.choice(['carlos capeto',"daniel caballero","tomas vargas","ana montes","luisa carmona"])
        fecha=random.choice(["12-04-23","12-04-24","12-04-25","12-05-2023","12-05-2025"])
        correo=random.choice(["carlosc@correo.com","daniel@correo.com","tomasvar@correo.com","anamon@correo.com","luisacar@correo.com"])
        
        
        
       


        encuesta=[corregimiento,hectareasSemabradas,especieSembrada,nombres,fecha,correo]

        datosSiembraArboles.append(encuesta)

    return datosSiembraArboles

print(listaDatosArboles())








# Siembra de arboles
""" corregimiento
hectareassembradas
nombres
fecha
correo """