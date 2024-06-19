import random

def generadorDatosVehicular():

    listaVehicular=[]
    for i in range(200):
        municipio=random.choice(["Sabaneta", "Envigado", "Poblado", "Bello", "Girardota"])
        tipoVehiculo=random.choice(["Moto", "Automovil","Camion","Bus","Tractocamion"])
        tipoCombustible=random.choice(["ACPM", "Corriente","Premiun","Electrico","Gas"])
        nombre=random.choice(["ana vega", "juan cruz", "gilberto montoya", "cecilia miranda", "paola vera"])
        fecha=random.choice(['2024-03-15','2024-04-16','2024-05-17','2024-04-20','sin'])
        correo = random.choice(["naVega@hotmail.com","juanCruz@gmail.com","gilberto@correo.com","ceci@hotmail.com","paola@gmail.com"])
        cantidadContaminacion= random.choice(["1","10","20","30","40","50","60","70","80","90","100"])
        

        encuesta=[municipio,tipoVehiculo,tipoCombustible,nombre,fecha,correo,cantidadContaminacion]

        listaVehicular.append(encuesta)

    return listaVehicular

print(generadorDatosVehicular())









