import os
import pickle
import random
import time
import PIL
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from keras import Input, Model
from keras import backend as K
from keras.callbacks import TensorBoard
from keras.layers import Dense, LeakyReLU, BatchNormalization, ReLU, Reshape, UpSampling2D, Conv2D, Activation, \
    concatenate, Flatten, Lambda, Concatenate
from keras.optimizers import Adam
from matplotlib import pyplot as plt

# --------------------------------------------------------
# load_dataset()
# --------------------------------------------------------
# Loads the image dataset into a pandas dataframe
# --------------------------------------------------------
def load_dataset():
    dataset = pd.read_parquet('metadata.parquet')
    return dataset

imageDataframe = load_dataset()

print("imageDataset Type: ", type(imageDataframe))
print(imageDataframe.head())


# deals with text input: skip thought vectors???



# --------------------------------------------------------
# build_generator()
# --------------------------------------------------------
# Builds generator
# --------------------------------------------------------
def build_generator():
    model = tf.keras.Sequential()
    # Add layers to generate images from text
    # ...
    return model

# --------------------------------------------------------
# build_discriminator()
# --------------------------------------------------------
# Builds generator
# --------------------------------------------------------
def build_discriminator():
    model = tf.keras.Sequential()
    # Add layers to classify real or generated images
    # ...
    # nat was here
    return model

# Create generator and discriminator
generator = build_generator()
discriminator = build_discriminator()