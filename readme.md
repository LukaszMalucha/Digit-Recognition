# Digit Recognition with Keras

### Try it yourself:
[Heroku App](https://digit-prediction.herokuapp.com/)


## PROJECT OVERVIEW

Hand-Written Digit Recognition based on MNIST Dataset. Convolutional Neural Network was built with Keras & Tensorflow(GPU). 
Heroku-hosted web application was built with Flask framework, Ajax & FileSaver. <br>

MNIST Dataset:<br>
[Dataset](http://yann.lecun.com/exdb/mnist/)


### Prediction
<br>

![img](https://user-images.githubusercontent.com/26208598/51791899-2fb01c00-21a2-11e9-9c92-ac9ab23d9e1a.JPG)

<br>


## TOOLS, MODULES & TECHNIQUES

##### Python – web development:
flask | Conda | Heroku | Docker
##### Python – CNN:
keras | tensorflow | scipy | numpy | h5py

##### Web Development:
Ajax | FileSaver.js | HTML | CSS | Bootstrap | Materialize

##### Database Development:
SQLite

##### Testing
selenium | unittest

## Test Suite:

### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/Digit-Recognition.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Digit-Recognition)

### Test Files:

##### /tests

## INSTALLING REQUIREMENTS (Conda Environment, Cloud9)

wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh<br>
chmod a+x Miniconda3-latest-Linux-x86_64.sh<br>
./Miniconda3-latest-Linux-x86_64.sh<br>

##### NEW TERMINAL

conda create -n py3 python=3 ipython <br>
source activate py3 <br>
pip install --upgrade pip<br>

##### CNN Build

pip install numpy <br>
conda install -c conda-forge tensorflow<br>
pip install keras==2.1.3<br>
pip install scipy <br>
pip install pillow<br>

##### Flask App Build

pip install flask<br>
pip install flask-boostrap<br>
pip install Flask-Uploads<br>

pip freeze --local > requirements.txt
<br>
<br>
##### Thank you,

Lukasz Malucha