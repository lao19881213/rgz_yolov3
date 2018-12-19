# rgz_yolov3

Radio Galaxy Zoo: CRAY - Radio Morphologies Classifing using Deep Learning

## Introduction

CRAY - Classifying Radio sources Automatically with Yolov3 - is a proof-of-concept radio source morphology classifier based upon the YOLOv3. CRAY is the first publicly available radio source morphology classifier that is capable of associating discrete and extended components of radio sources in an automated fashion. The promising results from CRAY have implications for the further development of efficient cross-wavelength source identification, matching, and morphology classifications for future radio surveys.


---

## Requirements

The code requires Tensorflow 1.12.0, python 3.6.3, Keras 2.1.5 as well as the following python libraries:
    matplotlib
    numpy
    opencv-python
    scipy
    cython
    easydict
    astropy
    Pillow
    pyyaml
	 
Those modules can be installed using: pip install -U pip followed by pip install -r requirements.txt. It is highly recommended to setup a standalone python virtual environment to install these modules and run the code.


---

## Setup

   1.Clone this repository: git clone 
   2.Download RGZ Data: cd data and run python download_data.py. This will download data for training, testing, and detection.


---

## Detection

   python yolo_video.py --image to detect a multi-component radio galaxy! Some examples of demo output are shown below:
  
Each detected box denotes an identified radio source, and its morphology is succinctly labelled as X C_Y P, where X and Y denotes the number of radio components and the number of radio peaks respectively. Each morphology label is also associated with a score between 0 and 1, indicating the probability of a morphology class being present.

---

## train

   1.python voc_annotation.py
   2.python train.py

To train your own RGZ model on GPU node managed by the SLURM job scheduler. You will need to change resources, paths, and module names based on the configuration of your own cluster.

##test results
<img src="https://github.com/lao19881213/rgz_yolov3/tree/master/output/FIRSTJ000007.0+081644_logminmax.png">

