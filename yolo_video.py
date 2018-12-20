import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import glob
import os
import time
import matplotlib.pyplot as plt


def detect_img(yolo):
    path = "comfig/*.png"
    outdir = "output"
    for jpgfile in glob.glob(path):
        img = Image.open(jpgfile)
        img, predicted_class, score, left, top, right, bottom = yolo.detect_image(img)
       # img = yolo.detect_image(img)
        print(jpgfile)
#    '''
#        plt.figure()
#        fig, ax = plt.subplots(1)
#        img = np.array(img)
#        ax.imshow(img)
#        plt.axis('off')
#        plt.gca().xaxis.set_major_locator(NullLocator())
#        plt.gca().yaxis.set_major_locator(NullLocator())
#        plt.savefig('output/%d.png' % (jpgfile), bbox_inches='tight', pad_inches=0.0)
#        plt.close()
#    '''
        img.save(os.path.join(outdir, os.path.basename(jpgfile)))
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
