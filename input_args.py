import getopt
import sys


def input_test_val(ar):
    output_image = ''
    input_image = ''
    try:
        opts, args = getopt.getopt(ar, "hi:o:", ["input_image=", "output_image="])
    except getopt.GetoptError:
        print('test_val.py -i <input_image> -o <output_image>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test_val.py -i <input_image> -o <output_image>')
            sys.exit()
        elif opt in ('-o', '--output_image'):
            output_image = arg
        elif opt in ('-i', '--input_image'):
            input_image = arg
    return input_image, output_image


def input_collect(ar):
    output_dir = ''
    input_dir = ''
    test_part = 0.15
    try:
        opts, args = getopt.getopt(ar, "hi:o:t:", ["input_dir=", "output_dir=", "test_part"])
    except getopt.GetoptError:
        print('collect_data.py -i <input_dir> -o <output_dir> -t <test_part>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('collect_data.py -i <input_dir> -o <output_dir> -t <test_part>')
            sys.exit()
        elif opt in ('-o', '--output_dir'):
            output_dir = arg
        elif opt in ('-i', '--input_dir'):
            input_dir = arg
        elif opt in ('-t', '--test_part'):
            test_part = arg
    return input_dir, output_dir, test_part


def input_train(ar):
    data_dir = ''
    checkpoint_dir = ''
    buffer_size = 400
    lambda_train = 100
    epochs = 150
    restore = False
    try:
        opts, args = getopt.getopt(ar, "hd:c:e:l:b:r:", ["data_dir=", "checkpoint_dir=", "epochs=", "lambda=",
                                                         "buffer_size=", "restore="])
    except getopt.GetoptError:
        print('train.py -d <data_dir> -c <checkpoint_dir> -e <epochs> -l <lambda> -b <buffer_size>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('train.py -d <data_dir> -c <checkpoint_dir> -e <epochs> -l <lambda> -b <buffer_size>')
            sys.exit()
        elif opt in ('-d', '--data_dir'):
            data_dir = arg
        elif opt in ('-c', '--checkpoint_dir'):
            checkpoint_dir = arg
        elif opt in ('-e', '--epochs'):
            epochs = arg
        elif opt in ('-l', '--lambda'):
            lambda_train = arg
        elif opt in ('-b', '--test_part'):
            buffer_size = arg
        elif opt in ('-r', '--restore'):
            restore = arg
    return data_dir, checkpoint_dir, buffer_size, lambda_train, epochs, restore
