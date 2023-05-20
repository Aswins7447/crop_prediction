from django.shortcuts import render, redirect
from django.http import HttpResponse

from sklearn.model_selection import train_test_split
from joblib import dump, load
import numpy as np  

from .models import Crop

loaded_model = load('model.joblib')

crops = {
    0: 'apple',
    1: 'banana',
    2: 'blackgram',
    3: 'chickpea',
    4: 'coconut',
    5: 'coffee',
    6: 'cotton',
    7: 'grapes',
    8: 'jute',
    9: 'kidneybeans',
    10: 'lentil',
    11: 'maize',
    12: 'mango',
    13: 'mothbeans',
    14: 'mungbean',
    15: 'muskmelon',
    16: 'orange',
    17: 'papaya',
    18: 'pigeonpeas',
    19: 'pomegranate',
    20: 'rice',
    21: 'watermelon'
}


# Create your views here.

def index(req):

    if req.method == 'GET':
        return render(req, 'index.html')

    elif req.method == 'POST':
        
        try:
            ph = float(req.POST['pH'])
            n  = float(req.POST['nitrogen'])
            p  = float( req.POST['phosphorous'])
            k  = float( req.POST['potassium'])
            temp = float( req.POST['temperature'])
            humidity = float( req.POST['humidity'])

            #printing the values got in console
            print(ph, n, p, k, temp, humidity)
            
            #predicting the crop
            input_attributes = np.array([[n, p, k, temp, humidity, ph]])
            crop_predicted = loaded_model.predict(input_attributes)
            crop_name      = crops[crop_predicted[0]]
            print(crop_name)

            #adding the data to Crop table
            new_crop = Crop(ph=6.5, nitrogen=50.0, phosphorous=25.0, potassium=30.0, temperature=28.0, humidity=80.0, crop=crop_name)
            new_crop.save()

            #return HttpResponse('The best crop to grow is '+ crops[crop_predicted[0]])
            return render(req, 'result.html', {'crop_name' : crop_name })

        except Exception as e:
            return HttpResponse('Invalid Input or Someother error occured!')

        
def get_sensor_data(request):
    print('Entered into get_sensor_data function....')
    return HttpResponse('Entered into get sensor function...')
