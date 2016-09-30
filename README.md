# Usage of the web demo

## Requirements

The demo server requires Python with some dependencies.
To make sure you have the dependencies, please run `pip install -r requirements.txt`, and also make sure that you have compiled the Python Caffe interface and that it is on your `PYTHONPATH`


## Prepare your caffe model.

Please refer to [Caffe](http://caffe.berkeleyvision.org/) for how to train a model based on your own dataset. After the train, you should get the net file .prototxt, the weight file .caffemodel.

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

