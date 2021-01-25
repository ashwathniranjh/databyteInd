from flask import Flask
import io
import numpy as np
from PIL import Image
import os
import keras
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.models import model_from_json
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from flask import request
from flask import jsonify
from flask import render_template

app = Flask(__name__, template_folder = 'static/templates')
def get_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    global loaded_model
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    print("model loaded!")
   

def preprocess_image(img_path):
    
    img = image.load_img(img_path, target_size  = (100,100));
    img1 = img_to_array(img)
    img2 = np.expand_dims(img1, axis = 0)
    x = preprocess_input(img2, mode = 'caffe')
    return x 

print("* Loading Keras Model.....")
get_model()


def predict(f):
   
    processed_image = preprocess_image(f)
    print(processed_image.shape)
    prediction = loaded_model.predict(processed_image)
    print("PREDICTION COMPLETED")
    prediction1 = prediction.tolist()
    print(prediction1)
    listOfChar = ['Iron Man', 'Captain America', 'Thor', 'Hulk', 'Black Widow']
    return listOfChar[prediction1[0].index(max(prediction1[0]))]
   
    
@app.route('/', methods=['GET'])
def index() :
    return render_template('index.html', prediction= "")

@app.route('/predict', methods = ['POST'])
def model_predict():
    
    f = request.files['Image']
    basepath = os.path.dirname(__file__)
    if f:
        filepath = os.path.join(
        basepath, 'static', 'uploads', f.filename
        )
    f.save(filepath)
    x = predict(filepath)
    print(x)
    prediction = x
    return render_template('predict.html', prediction= prediction, src = os.path.relpath(filepath, basepath))

if __name__ == '__main__':
    
    app.run(port = 5000, debug = True)
