import sys,os
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
import os
import cv2
from flask import Flask, Response
from flask_cors import CORS, cross_origin
import mss
import numpy as np


app = Flask(__name__)
CORS(app)
sct = mss.mss()


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"




@app.route("/")
def home():
    return render_template("index.html")



@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system("cd yolov5/ && python detect1.py --weights filtered_best11.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

        opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        result = {"image": opencodedbase64.decode('utf-8')}
        os.system("rm -rf yolov55/runs")

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)




@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:
        os.system("cd yolov5/ && python detect1.py --weights filtered_best11.pt --img 416 --conf 0.5 --source imagesd/620.png")
        os.system("rm -rf yolov5/runs")
        return "Camera starting!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")



if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=8080)
