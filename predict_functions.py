import tensorflow as tf
import numpy as np
from PIL import Image

IMAGE_SHAPE = 512


def load_image(image_file):
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image)

    input_image = tf.cast(image, tf.float32)
    input_image = (input_image / 127.5) - 1
    input_image = tf.reshape(input_image, [1, IMAGE_SHAPE, IMAGE_SHAPE, 3])
    return input_image


def predict(image):
    model = tf.keras.models.load_model('model/g512m.h5', compile=False)
    prediction = model(load_image(image), training=True)
    n_predict = ((prediction.numpy()[0] + 1) * 127.5).astype(np.uint8)
    img = Image.fromarray(n_predict)
    return img
