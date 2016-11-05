#Usage of the web demo

## Requirements

Install the [caffe](http://caffe.berkeleyvision.org/) framework following the instructions [here](http://caffe.berkeleyvision.org/installation.html), and also the Python caffe by runing the `Make pycaffe` and `pip install -r requirements.txt` in caffe/python. Make sure that you have compiled the Python Caffe interface and that it is on your `PYTHONPATH`

The demo server requires Python with some additional dependencies. To make sure you have the dependencies, please run `pip install -r requirements.txt`

## Prepare your caffe model.

Please refer to [Caffe](http://caffe.berkeleyvision.org/) for how to train a model based on your own dataset. After the train, you should get the net file .prototxt, the weight file .caffemodel.

## Example of how to train the dog breed model based on stanford dog dataset

Plese make sure your caffe framewok was installed, and the path of caffe/.build_release/tools has been added to the system PATH.

#### 1. Download the stanford dog dataset
    
Download the [images](http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar), [annotations](http://vision.stanford.edu/aditya86/ImageNetDogs/annotation.tar) and [lists](//vision.stanford.edu/aditya86/ImageNetDogs/lists.tar) from [stanford dogs dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/) and extract them to data/standord_dogs

#### 2. Parse the dataset to generate the train and test dataset

	cd data/standord-dogs && python dog_parse.py

#### 3. Creat the lmdb data for train

	cd data/standord-dogs && ./create_image.sh

#### 4. Train the model based on GoogleNet.

Download [GoogleNet Model](http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel) to models/bvlc_googlenet/

Run the following command to start the train. 

	cd models/bvlc_googlenet/ && train.sh

## How to config the web service. 

1. You could store your caffe mdoel in the models dir.

2. Modify the web_demo/app.py file. 

   a). In line 10, define the path that you store this project. 

   b). define your caffe model path from line 101 t0 108.


## Run

Running `python web_demo/app.py` will bring up the demo server, accessible at `http://0.0.0.0:5000`.
You can enable debug mode of the web server, or switch to a different port:

    % python examples/web_demo/app.py -h
    Usage: app.py [options]

    Options:
      -h, --help            show this help message and exit
      -d, --debug           enable debug mode
      -p PORT, --port=PORT  which port to serve content on
      -g, --gpu             enable GPU accelerator

