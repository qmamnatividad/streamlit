import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('weather_classification.h5')
  return model
model=load_model()
st.write("""
# Weather Classification"""
)
file=st.file_uploader("Upload a weather photo from your computer.",type=["jpg","png"])

import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(60,60)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image related to weather.")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names = ['Cloudy', 'Rain', 'Shine', 'Sunrise']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)
