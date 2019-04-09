from flask import render_template, request, Blueprint, session

from scipy.misc import imread, imresize
import numpy as np

import os
import base64
import re
import sys

## BLUEPRINT INIT

algorithms_blueprint = Blueprint(
    'algorithms', __name__,
    template_folder="templates"
)

from .load import init_model

sys.path.append(os.path.abspath(",/model"))

global model, graph
model, graph = init_model()


## Image Converter from str to b64
def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)', imgData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))


@algorithms_blueprint.route('/')
def dashboard():
    """Homepage View"""

    return render_template("dashboard.html")


@algorithms_blueprint.route('/predict', methods=['GET', 'POST'])
def predict():
    imgData = request.get_data()

    ## transform
    convertImage(imgData)
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x, (28, 28))
    x = x.reshape(1, 28, 28, 1)
    ## predict
    with graph.as_default():
        out = model.predict(x)
        print(np.argmax(out, axis=1))
        response = np.array_str(np.argmax(out, axis=1))
        response = ' '.join(map(str, response))
        response = response.replace('[', '')
        response = response.replace(']', '')
        return response
