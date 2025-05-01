
from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
model = tf.keras.models.load_model('model/crop_model.h5')
classes = ['Healthy', 'Disease', 'Pest', 'Water Stress']

@app.route('/predict', methods=['POST'])
def predict():
    image = Image.open(request.files['image']).resize((224, 224))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    prediction = model.predict(img_array)
    return jsonify({'prediction': classes[np.argmax(prediction)]})

if __name__ == '__main__':
    app.run(debug=True)
