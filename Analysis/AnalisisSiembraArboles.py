import pandas as pd
import matplotlib.pyplot as plt

from data.generators.generadorSiembraArboles import listaDatosArboles
from helpers.crearTablaSiembraArbolesHTML import crearTabla

def construirSiembraArbolesDataFrame():
    datosSiembraArboles = listaDatosArboles()
    
    # Generamos el DataFrame
    SiembraArbolesDataFrame = pd.DataFrame(datosSiembraArboles, columns=["corregimiento", "hectareasSembradas", "especieSembrada", "nombres", "fecha", "correo"])
    print(SiembraArbolesDataFrame)
    
    # Generamos el recurso HTML    
    crearTabla(SiembraArbolesDataFrame, "datosSiembraArboles") 
    
    # Limpiando el DataFrame
    SiembraArbolesDataFrame.replace('sin', pd.NA, inplace=True)
    SiembraArbolesDataFrame.dropna(inplace=True)
    
    # Filtrar DATOS
    filtroSiembraArbolesBueno = SiembraArbolesDataFrame.query("(hectareasSembradas >= 6) and (hectareasSembradas < 8)").value_counts()
    filtroSeimbraArbolesAceptable = SiembraArbolesDataFrame.query("(hectareasSembradas >= 4) and (hectareasSembradas < 6)").value_counts()
    filtroSiembraArbolesMalo = SiembraArbolesDataFrame.query("(hectareasSembradas >= 1) and (hectareasSembradas < 3)").value_counts()
    print("\n")
    
    # ORDENANDO LOS DATOS PARA GRAFICARLOS 
    datosOrdenadosSiembraArboles = SiembraArbolesDataFrame.groupby('corregimiento')['hectareasSembradas'].mean()
    
    # Graficando la información
    plt.figure(figsize=(20, 20))
    datosOrdenadosSiembraArboles.plot(kind='bar', color='blue')
    plt.title("Índice de cantidad de hectáreas sembradas por corregimientos de Medellín")
    plt.xlabel("Corregimiento")
    plt.ylabel("Hectáreas Sembradas")
    plt.grid(True)
    plt.savefig("./assets/img/siembraArboles.png", format='png', dpi=300)

construirSiembraArbolesDataFrame()
