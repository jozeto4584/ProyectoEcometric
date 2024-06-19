import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorContaminacionReciclaje import generadorDatosReciclaje
from helpers.crearTablareciclajeHTML import crearTabla

def construirContaminacionReciclajeDataFrame():
    datosReciclaje = generadorDatosReciclaje()
    
    # Generamos el DataFrame
    ReciclajeDataFrame = pd.DataFrame(datosReciclaje, columns=["barrio", "tipoReciclaje", "tiempoSemana", "nombre", "fecha"])
    print(ReciclajeDataFrame)   
    
    # Generamos el recurso HTML    
    # crearTabla(ReciclajeDataFrame, "datosReciclaje")  # No está definido en tu código proporcionado, puede comentarse si no se utiliza
    
    # Limpiando el DataFrame
    ReciclajeDataFrame.replace('sin', pd.NA, inplace=True)
    ReciclajeDataFrame.dropna(inplace=True)
    
    # Filtrando datos
    filtroReciclajeBueno = ReciclajeDataFrame.query("(tiempoSemana >= 15) and (tiempoSemana < 30)").value_counts()
    filtroReciclajeAceptable = ReciclajeDataFrame.query("(tiempoSemana >= 5) and (tiempoSemana < 15)").value_counts()
    filtroReciclajeMalo = ReciclajeDataFrame.query("(tiempoSemana >= 1) and (tiempoSemana < 5)").value_counts()
    print("\n")
    
    # ORDENANDO LOS DATOS PARA GRAFICARLOS 
    datosOrdenadosReciclaje = ReciclajeDataFrame.groupby('barrio')['tiempoSemana'].mean()
    
    # Graficando la información
    plt.figure(figsize=(20, 20))
    datosOrdenadosReciclaje.plot(kind='bar', color='blue')
    plt.title("Índice de contaminación por basuras en los barrios de Medellín")
    plt.xlabel("Barrio")    
    plt.ylabel("Tiempo Semana")
    plt.grid(True)
    plt.savefig("./assets/img/reciclajeContaminacion.png", format='png', dpi=300)

construirContaminacionReciclajeDataFrame()


