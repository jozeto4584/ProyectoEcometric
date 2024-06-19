import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadocontaminacionrRuido import generadorDatosRuido
from helpers.crearTablaRuidoHTML import crearTabla

def construirContaminacionRuidoDataFrame():
    datosRuido = generadorDatosRuido()
    
    # Generamos el DataFrame
    datosRuidoDataFrame = pd.DataFrame(datosRuido, columns=["comuna", "nombre", "dBdiurnos", "dBnocturnos", "fecha"])
    print(datosRuidoDataFrame)
    
    # Generamos el recurso HTML
    # crearTabla(datosRuidoDataFrame, "datosRuido")
    
    # Limpiando el DataFrame
    datosRuidoDataFrame.replace('sin', pd.NA, inplace=True)
    datosRuidoDataFrame.dropna(inplace=True)
    
    # Filtrando datos
    filtroCalidadRuidoBueno = datosRuidoDataFrame.query("(dBdiurnos >= 20) and (dBdiurnos < 60)").value_counts()
    filtroCalidadRuidoAceptable = datosRuidoDataFrame.query("(dBdiurnos >= 60) and (dBdiurnos < 80)").value_counts()
    filtroCalidadRuidoMalo = datosRuidoDataFrame.query("(dBdiurnos >= 80) and (dBdiurnos < 140)").value_counts()
    print("\n")
    
    # ORDENANDO LOS DATOS PARA GRAFICARLOS
    datosOrdenadosRuido = datosRuidoDataFrame.groupby('comuna')['dBdiurnos'].mean()
    
    # Graficando la información
    plt.figure(figsize=(20, 20))
    datosOrdenadosRuido.plot(kind='bar', color='green')
    plt.title("Índice de contaminación auditiva por comunas de Medellín")
    plt.xlabel("Comuna")
    plt.ylabel("dBdiurnos")
    plt.grid(True)
    plt.savefig("./assets/img/datosRuido.png", format='png', dpi=300)

construirContaminacionRuidoDataFrame()
