from PIL import Image

IMAGE_SHAPE = 512


def image_calc_size(width, height, train):
    if train:
        width, height = height, width
    r = width / height
    if width > height:
        return IMAGE_SHAPE, int(IMAGE_SHAPE / r)
    return int(IMAGE_SHAPE * r), IMAGE_SHAPE


def image_crop(img):
    n_img = Image.new(mode="RGB", size=(IMAGE_SHAPE, IMAGE_SHAPE))
    shift_x, shift_y = int((IMAGE_SHAPE - img.size[0]) / 2), int((IMAGE_SHAPE - img.size[1]) / 2)
    n_img.paste(img, (shift_x, shift_y, img.size[0] + shift_x, img.size[1] + shift_y))
    return n_img


def image_prepare(img_path):
    img = Image.open(img_path)
    img = img.resize(image_calc_size(img.size[0], img.size[1], False))
    width, height = img.size
    img = image_crop(img)
    img.save('data/input.jpg')
    return width, height
