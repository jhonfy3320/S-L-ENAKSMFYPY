'''from gettext import npgettext
import joblib
import numpy as pd 

# importar nuestra nuevas librerias 
from flask import Flask
from flask import jsonify

from models import Models # herramienta para trabajar con archivos json

# Comfigurando nuestro servidor 
app = Flask(__name__)

#definiendo la ruta de contestacion 
#POSMAN PARA PRUEBAS 
@app.route('/predict', methods=['GET'])

def predict():
    X_test = npgettext.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    prediction = Models.predict(X_test.reshape(1,-1))
    return jsonify({'prediccion' : list(prediction)})

#Corriendo todo nuetro proyecto desde este archivo; Corriendo como el Principal 
if __name__ == '__main__':
    model  = joblib.load('./models/best_model.pkl')
    #al dar run en nuetro puerto simpre debemos utilizar puertos mas altos, ya que los puetos balos son utilizados por el sistemas operativo 
    app.run(port=8080)

'''
'''from flask import Flask, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo previamente entrenado
model = joblib.load('./models/best_model.pkl')

# POSTMAN PARA PRUEBAS
@app.route('/predict', methods=['POST'])
def predict():
    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    prediction = model.predict(X_test.reshape(1, -1))
    return jsonify({'prediccion': list(prediction)})

if __name__ == "__main__":
    app.run(port=5000)'''



