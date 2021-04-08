import sys
import os
from collect_data import image_calc_size
from input_args import input_test_val
import tensorflow as tf
import numpy as np
from PIL import Image

IMAGE_SHAPE = 512
input_image, output_image, model_dir = input_test_val(sys.argv[1:])
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)
dir_list = ['model/', 'local']


def load_image(image_file):
    image = tf.io.read_file(image_file)
    image = tf.image.decode_jpeg(image)

    in_img = tf.cast(image, tf.float32)
    in_img = (in_img / 127.5) - 1
    in_img = tf.reshape(in_img, [1, IMAGE_SHAPE, IMAGE_SHAPE, 3])
    return in_img


def image_extension(image):
    n_img = Image.new(mode="RGB", size=(IMAGE_SHAPE, IMAGE_SHAPE))
    shift_x, shift_y = int((IMAGE_SHAPE - image.size[0]) / 2), int((IMAGE_SHAPE - image.size[1]) / 2)
    n_img.paste(image, (shift_x, shift_y, image.size[0] + shift_x, image.size[1] + shift_y))
    return n_img


def image_prepare(img_path):
    image = Image.open(img_path)
    image = image.resize(image_calc_size(image.size[0], image.size[1], False))
    w, h = image.size
    image = image_extension(image)
    image.save('local/input.jpg')
    return w, h


if __name__ == '__main__':
    for path_dir in dir_list:
        if not os.path.exists(path_dir):
            os.mkdir(path_dir)
    width, height = image_prepare(input_image)
    model = tf.keras.models.load_model(model_dir, compile=False)
    prediction = model(load_image('local/input.jpg'), training=True)
    n_predict = ((prediction.numpy()[0] + 1) * 127.5).astype(np.uint8)
    img = Image.fromarray(n_predict)
    img = img.crop(((IMAGE_SHAPE - width) / 2, (IMAGE_SHAPE - height) / 2,
                    (IMAGE_SHAPE - width) / 2 + width, (IMAGE_SHAPE - height) / 2 + height))
    img.save(output_image, quality=100)
