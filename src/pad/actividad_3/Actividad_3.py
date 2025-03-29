import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import io

class actividad3:
    def __init__(self, ruta_dataset=""):
        self.ruta_raiz=os.path.abspath(os.getcwd())
        self.ruta_act3 = "{}/src/pad/actividad_3/".format(self.ruta_raiz)
        datos = {
            "n_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            "detalle":["Crea un DataFrame frutas que luzca así","Crea un DataFrame ventas_frutas que coincida con el diagrama","Crea una variable utensilios con una Serie que tenga el siguiente aspecto","Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura","Visualiza las primeras filas del DataFrame","Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?","¿Cuál es el precio promedio?","Cuál es el precio más alto pagado","Crea un DataFrame con todos los vinos de california Salida","Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico","¿Cuáles son los tipos de uva más comunes en California?","¿Cuáles son los 10 tipos de uva más comunes en California?"],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],
            
        }
        self.df = pd.DataFrame(datos)
        self.df["resultado"] = self.df["resultado"].astype(object)
        print(self.ruta_raiz)
        try:
            ruta_dset="{}/src/pad/actividad_3/winemag-data-130k-v2.csv/".format(self.ruta_raiz)
            self.review=pd.read_csv(ruta_dset)
            print("Se ha cargado el dataset")
        except:
            print("No se ha podido cargar el dataset")
            self.review=pd.DataFrame()
        
            
        
    def punto_1(self):
        data= {
            "granadilla": [20],
            "tomates": [50]
        }
        df_1= pd.DataFrame(data)
        df_1.to_csv("src/pad/actividad_3/frutas.csv")
        self.df.loc[0,"resultado"] = "src/pad/actividad_3/frutas.csv"
        print("punto_1")     

    def punto_2(self):
        data = {
            "Granadilla": [20, 49],
            "Tomates": [50, 100], 
            } 
        df_2= pd.DataFrame(data, index=["Ventas 2021", "Ventas 2022"])
        df_2.to_csv("src/pad/actividad_3/ventas_frutas.csv")
        self.df.loc[1,"resultado"] = "src/pad/actividad_3/frutas.csv"
        print("punto_2") 

    def punto_3(self):
        utencilios= pd.Series(
            data=["3 unidades","2 unidades","4 unidades","5 unidades"],
            index=["Cuchara","Tenedor","Cuchillo","Plato"],
            name="cocina")
        df_3= pd.DataFrame(utencilios)
        df_3.to_csv("src/pad/actividad_3/utencilios.csv")
        self.df.loc[2,"resultado"] = "src/pad/actividad_3/utencilios.csv"
        print("punto_3") 

    def punto_4(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_4=pd.read_csv(ruta_dset)
        primeros_5 = df_4.head(5)
        ultimos_5 = df_4.tail(5) 
        df_combinado = pd.concat([primeros_5, ultimos_5]) 
        df_combinado.to_csv("src/pad/actividad_3/primeras_ultimas_fi las.csv")
        self.df.loc[3,"resultado"] = "src/pad/actividad_3/winemag-data-130k-v2.csv"
        print(df_combinado)
              
    def punto_5(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_5=pd.read_csv(ruta_dset)
        primeros_5 = df_5.head(5)
        primeros_5.to_csv("src/pad/actividad_3/primeros_5.csv")
        self.df.loc[4,"resultado"] = "src/pad/actividad_3/primeros_5.csv"
        print("primeros_5") 


    def punto_6(self): 
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_6=pd.read_csv(ruta_dset)
        buffer = io.StringIO()
        df_6.info(buf=buffer)
        entrada = buffer.getvalue()
        num_entradas_line = [line for line in entrada.splitlines() if "RangeIndex" in line][0]
        num_entradas = int(num_entradas_line.split(":")[1].strip().split(" ")[0])
        resultado = f"{entrada}\nNúmero de entradas encontradas: {num_entradas}"
        self.df.loc[5,"resultado"] = num_entradas       
        print("Completo el punto 6 : ok")
        return num_entradas
  

    def punto_7(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_7=pd.read_csv(ruta_dset)
        precio_promedio = df_7["price"].mean()
        self.df.loc[6,"resultado"] = precio_promedio
        print("punto_7") 

    def punto_8(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_8=pd.read_csv(ruta_dset)
        precio_maximo = df_8["price"].max()
        self.df.loc[7,"resultado"] = precio_maximo
        print("punto_8") 

    def punto_9(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_9=pd.read_csv(ruta_dset)
        df_california = df_9[df_9["province"] == "California"]
        df_california.to_csv("src/pad/actividad_3/vinos_california.csv")
        self.df.loc[8,"resultado"] = "src/pad/actividad_3/vinos_california.csv"
        print("punto_9") 

    def punto_10(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_10=pd.read_csv(ruta_dset)
        indice_maximo = df_10["price"].idxmax()
        vino_maximo = df_10.loc[indice_maximo]
        resultado = f"Índice del vino con el precio más alto: {indice_maximo}\nInformación del vino:\n{vino_maximo}"
        self.df.loc[9,"resultado"] = resultado
        print("punto_10") 

    def punto_11(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_11=pd.read_csv(ruta_dset)
        vinos_california = df_11[df_11["province"] == "California"]
        conteo_variedades = vinos_california["variety"].value_counts()
        self.df.loc[10,"resultado"] = f"{conteo_variedades}"
        print("punto_11") 

    def punto_12(self):
        ruta_dset="src/pad/actividad_3/winemag-data-130k-v2.csv"
        df_12=pd.read_csv(ruta_dset)
        uvas_california = df_12[df_12["province"] == "California"]
        conteo_variedades = uvas_california["variety"].value_counts()
        conteo_variedades = conteo_variedades.head(10)
        self.df.loc[11,"resultado"] = f"{conteo_variedades}"
        print("punto_12") 
    
    def ejecutar(self):
        self.punto_1()     
        self.punto_2() 
        self.punto_3() 
        self.punto_4() 
        self.punto_5() 
        self.punto_6() 
        self.punto_7() 
        self.punto_8() 
        self.punto_9() 
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.df.to_csv("actividad3.csv")
        
act = actividad3()
#act. punto_6()
act.ejecutar()