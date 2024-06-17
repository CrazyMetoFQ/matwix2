from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import PIL.Image


import sys
sys.path.insert(1, "C:/Users/alima/OneDrive/Documents/GitHub/matwix2/")
import helperlibs.imgtoolscustum as imgtools


import keras
from cv2 import resize as cv2resize
from cv2 import INTER_NEAREST as cv2resizeINTER
import numpy


DVALS = {'(':0, ')':1, '+':2, '-':3, '0':4, '1':5,
         '2':6, '3':7, '4':8, '5':9, '6':10, '7':11,
         '8':12, '9':13, '=':14, '[divideforward]':15,
         '[multiply]':16}
DVALS = {v: k for k, v in DVALS.items()}


MODEL = model = keras.models.load_model("C:/Users/alima/OneDrive/Documents/GitHub/matwix2/aipart/nnmodel/take2/savedmodel.keras")




app = Flask(__name__)

# Define upload folder path
UPLOAD_FOLDER = r'C:\Users\alima\OneDrive\Documents\GitHub\matwix2\website\static\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():

    if len(request.files) == 0:
        return 'No file uploaded!', 400

    print(request.files)
    file = request.files["imageUpload"]
    if file.filename == '':
        return 'No selected file', 400

    # Secure filename to avoid conflicts
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Display uploaded image path
    return render_template('index.html', filename=filename)



global SPLITOPTIONS_stuf

SPLITOPTIONS_stuf = [0,0,0]

@app.route("/img_mod/<imgname>", methods = ['POST', 'GET'])
def main_Img_stuff_upload(imgname):

    
    img = PIL.Image.open(os.path.join(app.config['UPLOAD_FOLDER'], imgname)).convert("L")
    img = imgtools.convert_img_2bw(img)
    subimgs = imgtools.split_img_woDuplicate(img)
    
    resozed_subimgs = [numpy.expand_dims(cv2resize(im, (50,50), interpolation=cv2resizeINTER), axis=0) for im in subimgs]
    
    predictions = [DVALS[numpy.argmax(MODEL.predict(im))] for im in resozed_subimgs]
    
    subimgs = [(subimg-1)*-255 for subimg in subimgs]
    imgf= imgtools.combine_images_row(subimgs)
    imgf.save(os.path.join(app.config['UPLOAD_FOLDER'], imgname.split(".")[0]+"_mod1.png"))
    

    modimgnm = imgname.split(".")[0]+"_mod1.png"
    return render_template('img_mod.html', imgname=imgname, modded_img_name=modimgnm, computed_values=str(predictions))
  
  

  
if __name__ == '__main__':
    app.run(debug=True)
