#utilidades 
#tener todos los metodos que vamos a reutilizar en varias ocaciones  sobre los datos a lo largo de todo el proceso 
# Un ejemplo muy claro es el escalamiento 
from os import path
from turtle import pd
import pandas as pd  
import joblib


class Utils:
    def  load_from_csv(self): #Todas la funciones que estan dentro de una clase deben llevar el atributo SELF
        return pd.read_csv(path)

    def load_from_mysql(self):
        pass

    def features_target(self, dataset, drop_cols, y):
        X = dataset.drop(drop_cols, axis=1)
        y = dataset[y]
        return X,y
    

    def model_export(self, clf, score):
        print(score)
        joblib.dump(clf, './models/best_model.pkl')