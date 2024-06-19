import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorContaminacionVehicular import generadorDatosVehicular
from helpers.crearTablavehiculosHTML import crearTabla

def construirContaminacionVehicularDataFrame():
    datosvehicular = generadorDatosVehicular()
    
    # Generamos el DataFrame
    vehicularDataFrame = pd.DataFrame(datosvehicular, columns=["municipio", "tipoVehiculo", "tipoCombustible", "nombre", "fecha", "correo", "cantidadContaminacion"])
    
    # Generamos el recurso HTML    
    # crearTabla(vehicularDataFrame, "datosvehicular") 
    
    # Limpiando el DataFrame
    vehicularDataFrame.replace('sin', pd.NA, inplace=True)
    vehicularDataFrame.dropna(inplace=True)
    
    # Convertir la columna 'cantidadContaminacion' a valores numéricos
    vehicularDataFrame['cantidadContaminacion'] = pd.to_numeric(vehicularDataFrame['cantidadContaminacion'], errors='coerce')
    vehicularDataFrame.dropna(subset=['cantidadContaminacion'], inplace=True)
    
    # Ordenando los datos para graficarlos
    datosOrdenadosvehicular = vehicularDataFrame.groupby('municipio')['cantidadContaminacion'].mean()
    
    # Graficar la información
    plt.figure(figsize=(20, 20))
    datosOrdenadosvehicular.plot(kind='bar', color='orange')
    plt.title("Índice de contaminación vehicular por barrios de Medellín")
    plt.xlabel("Municipio")
    plt.ylabel("Cantidad de Contaminación")
    plt.grid(True)
    plt.savefig("./assets/img/calidadVehicular.png", format='png', dpi=300)

construirContaminacionVehicularDataFrame()
