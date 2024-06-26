from utils import Utils
from models import Models

#main.py se encarga de controlar todo el flujo del codigo 
#Preguntar si este se esta ejecutando de primeras 
if __name__ == '__main__':
    
    utils = Utils()
    models = Models()

    data = utils.load_from_csv('./in/felicidad.csv')
    X, y = utils.features_target(data, ['score', 'rank', 'country'],['score'])
    models.grid_training(X,y)
    print(data)

   # data = utils.load_from_mysql()