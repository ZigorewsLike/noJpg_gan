import getopt
import sys
import os
from image_functions import *
from predict_functions import *

argv = sys.argv[1:]
IMAGE_SHAPE = 512
input_image = ""
output_image = ""
dir_list = ['data/', 'model/']

try:
    opts, args = getopt.getopt(argv, "hi:o:", ["input_image=", "result_image="])
except getopt.GetoptError:
    print('main.py -i <input_image> -o <result_image>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('main.py -i <input_image> -o <result_image>')
        sys.exit()
    elif opt in ('-o', '--result_image'):
        output_image = arg
    elif opt in ('-i', '--input_image'):
        input_image = arg


if __name__ == '__main__':
    for path_dir in dir_list:
        if not os.path.exists(path_dir):
            os.mkdir(path_dir)
    width, height = image_prepare(input_image)
    img = predict('data/input.jpg')
    img.crop(((IMAGE_SHAPE - width) / 2, (IMAGE_SHAPE - height) / 2,
              (IMAGE_SHAPE - width) / 2 + width, (IMAGE_SHAPE - height) / 2 + height))
    img.save(output_image, quality=100)
