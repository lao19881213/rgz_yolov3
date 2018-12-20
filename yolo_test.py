import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import glob
import os
import time
import matplotlib.pyplot as plt


def detect_img(yolo):
    image_ids = open('VOC2007/ImageSets/Main/test.txt').read().strip().split()
   # path = "comfig/*.png"
    outdir = "output"
    list_file1 = open('VOC2007/1C_1P.txt', 'w')
    list_file2 = open('VOC2007/1C_2P.txt', 'w')
    list_file3 = open('VOC2007/1C_3P.txt', 'w')
    list_file4 = open('VOC2007/2C_2P.txt', 'w')
    list_file5 = open('VOC2007/2C_3P.txt', 'w')
    list_file6 = open('VOC2007/3C_3P.txt', 'w')

    for image_id in image_ids:
        img = Image.open('VOC2007/JPEGImages/%s.png'%(image_id))
        img, predicted_class, score, left, top, right, bottom = yolo.detect_image(img)
        for cl in range(len(predicted_class)):
            if predicted_class[cl] == "1C_1P":
               list_file1.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file1.write('\n')
            elif predicted_class[cl] == "1C_2P":
               list_file2.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file2.write('\n')
            elif predicted_class[cl] == "1C_3P":
               list_file3.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file3.write('\n')
            elif predicted_class[cl] == "2C_2P":
               list_file4.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file4.write('\n')
            elif predicted_class[cl] == "2C_3P":
               list_file5.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file5.write('\n')
            elif predicted_class[cl] == "3C_3P":
               list_file6.write('%s.png %f %s %s %s %s'  %(image_id,score[cl], left[cl], top[cl], right[cl], bottom[cl]))
               list_file6.write('\n')

    list_file1.close()
    list_file2.close()
    list_file3.close()
    list_file4.close()   
    list_file5.close()
    list_file6.close()

    # img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        '--input', nargs='?', type=str,required=False,default='comfig',
        help = "Video input path"
    )

    parser.add_argument(
        '--output', nargs='?', type=str, default='output',
        help = "[Optional] Video output path"
    )

    FLAGS = parser.parse_args()

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    else:
        print("Must specify at least video_input_path.  See usage with --help.")

