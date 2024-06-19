import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorcontaminacionAire import generarDatosCalidadAire
from helpers.crearTablaaireHTML import crearTabla

def construirAireDataFrame():
    datosAire = generarDatosCalidadAire()
    
    # Generamos el DataFrame
    aireDataFrame = pd.DataFrame(datosAire, columns=['nombre','comuna','ica','fecha','correo'])
    
    #generamos el recurso HTML    
    crearTabla (aireDataFrame,"datosaire") 
    
    # Limpiando el DataFrame (descomentar si es necesario)
    #reeplazando valores
    aireDataFrame.replace('sin',pd.NA,inplace=True)
    #elimino los registros que no cumplen el criterio
    aireDataFrame.dropna(inplace=True)
    
    #filtrar DATOS
    #Filtrar es aplicar condiciones logicas
    #que permitan analizar la informacion del DF
    filtroCalidadAireBueno=aireDataFrame.query("(ica>=10)and(ica<40)").value_counts()
    filtroCalidadAireAceptable=aireDataFrame.query("(ica>=40)and(ica<50)").value_counts()
    filtroCalidadAireMalo=aireDataFrame.query("(ica>=50)and(ica<100)").value_counts()
    print("\n")
   #ORDENANDO LOS DATOS PARA GRAFRICARLOS 
    datosOrdenadosAire=aireDataFrame.groupby('comuna')['ica'].mean()
  
    
    #grafico la informacion
    plt.figure(figsize=(20,20))
    datosOrdenadosAire.plot(kind='bar',color='green')
    plt.title("indice de contaminacion del aire por comuna en medellin")
    plt.xlabel("Comuna")
    plt.ylabel("ICA")
    plt.grid(True)
    plt.savefig("./assets/img/calidadaire.png",format='png',dpi=300)
    
     
construirAireDataFrame()