import getopt
import sys


def input_test_val(ar):
    output_image = ''
    input_image = ''
    try:
        opts, args = getopt.getopt(ar, "hi:o:", ["input_image=", "result_image="])
    except getopt.GetoptError:
        print('test_val.py -i <input_image> -o <result_image>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test_val.py -i <input_image> -o <result_image>')
            sys.exit()
        elif opt in ('-o', '--result_image'):
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
        elif opt in ('-o', '--input_dir'):
            output_dir = arg
        elif opt in ('-i', '--output_dir'):
            input_dir = arg
        elif opt in ('-t', '--test_part'):
            test_part = arg
    return input_dir, output_dir, test_part
