from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np
import tensorflow as tf
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array

app = Flask(__name__)

model = load_model("/Users/danielrangel/Library/Mobile Documents/com~apple~CloudDocs/_MAESTRIA/TFM/Production/Model_PROD.h5")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():


        imagefile = request.files["imagefile"]
        image_path = "/Users/danielrangel/Library/Mobile Documents/com~apple~CloudDocs/_MAESTRIA/TFM/Production/images/" + imagefile.filename
        imagefile.save(image_path)
    
    
        image = load_img(image_path, target_size=(150, 150))
        image = img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        
        
        pred = model.predict(image)
        pred = pred[0][0]
        if pred ==1 :
            predout = "A child still inside! please return to your vehicle"
            return render_template("NOK.html", prediction = predout)
        else :
            predout = "No Child left behind  :) "
            return render_template("OK.html", prediction = predout)
    
    
        



if __name__ == "__main__":
    app.run()