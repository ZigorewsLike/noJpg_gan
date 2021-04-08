from PIL import Image, ImageFile
import os
from shutil import copy
import random
import sys
from input_args import input_collect
c = 0
c_tr = 1
c_ts = 1
IMAGE_SHAPE = 512
ImageFile.LOAD_TRUNCATED_IMAGES = True


def image_calc_size(width, height, train):
    r = width / height
    new_width, new_height = IMAGE_SHAPE, int(IMAGE_SHAPE / r)
    new_width2, new_height2 = int(IMAGE_SHAPE * r), IMAGE_SHAPE
    if train:
        new_width, new_height, new_width2, new_height2 = new_width2, new_width, new_height2, new_height
    if width > height:
        return new_width, new_height
    return new_width2, new_height2


def image_crop(image):
    width, height = image.size
    _min = min(width, height)
    return image.crop(((width - _min) / 2, (height - _min) / 2, (width - _min) / 2 + _min, (height - _min) / 2 + _min))


if __name__ == '__main__':
    input_dir, output_dir, test_part = input_collect(sys.argv[1:])
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    for folder in ['data', 'train', 'val']:
        if not os.path.exists(os.path.join(output_dir, folder)):
            os.mkdir(os.path.join(output_dir, folder))

    for root, directories, files in os.walk(input_dir):
        for file in files:
            try:
                img = Image.open(os.path.join(input_dir, file))
                if img.size[0] < 600 or img.size[1] < 600:
                    continue
                img = img.resize(image_calc_size(img.size[0], img.size[1], True))
            except Exception:
                print(file)
                continue
            img2 = image_crop(img)
            img2_n = img2.resize((IMAGE_SHAPE // 2, IMAGE_SHAPE // 2))
            try:
                img2_n.save('local/test.jpg', quality=(random.randrange(20, 70)))
            except Exception:
                print('skip', file)
                continue
            img1 = Image.open('local/test.jpg')
            img1 = img1.resize((IMAGE_SHAPE, IMAGE_SHAPE))
            c += 1
            new_img = Image.new(mode="RGB", size=(IMAGE_SHAPE * 2, IMAGE_SHAPE))
            new_img.paste(img1, (0, 0, IMAGE_SHAPE, IMAGE_SHAPE))
            new_img.paste(img2, (IMAGE_SHAPE, 0, IMAGE_SHAPE * 2, IMAGE_SHAPE))
            new_img.save(os.path.join(os.path.join(output_dir, 'data'), str(c) + '.jpg'), quality=100, subsampling=0)
            if c % 100 == 0:
                print(' ', c / len(files) * 100, "%")
            img1.close()
    print('train/test sample generate')
    for root, directories, files in os.walk(os.path.join(output_dir, 'data')):
        files_test = random.sample(files, int(len(files) * int(test_part)))
        for file in files:
            if file in files_test:
                copy(os.path.join(os.path.join(output_dir, 'data'), file),
                     os.path.join(os.path.join(output_dir, 'test'), str(c_ts) + '.jpg'))
                c_ts += 1
            else:
                copy(os.path.join(os.path.join(output_dir, 'data'), file),
                     os.path.join(os.path.join(output_dir, 'train'), str(c_tr) + '.jpg'))
                c_tr += 1
