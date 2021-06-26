import os
import argparse

from PIL import Image
from tqdm.auto import tqdm

def change_color_of_logo(RGB:tuple, file='../logos/bblue.png'):

    assert isinstance(RGB, tuple), f"RGB should be tuple, currently got {type(RGB)}"

    img = Image.open(file)
    r_, g_, b_, _ = img.getpixel((500, 500))

    for x in tqdm(range(img.size[0])):
        for y in range(img.size[1]):
            r,g,b,a = img.getpixel((x, y))

            if (r,g,b) == (r_, g_, b_):

                r, g, b, a = (*RGB, a)
                newrgb = (r, g, b, a)
                img.putpixel((x, y), newrgb)

    return img

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--rgb", help="new rgb value.", nargs="+", type=int) 
    parser.add_argument("-o", "--output", help="filepath for logo in new color.", nargs='?', default='newlogo.png')

    args = parser.parse_args()
    
    new_rgb_tuple = tuple(args.rgb)
    outputpath = args.output

    newimg = change_color_of_logo(new_rgb_tuple)
    newimg.save(outputpath)