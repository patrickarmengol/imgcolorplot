# visualize the rgb color space box of an image
# TODO: exception handling, figure out why the saved figure looks so much worse than shown

import matplotlib.pyplot as plt
import argparse
from PIL import Image


def imgcolorplot(img, out=None):
    px = img.load()
    width, height = img.size
    
    ax = plt.axes(projection = '3d')
    ax.set_xticks([0, 127.5, 255])
    ax.set_yticks([0, 127.5, 255])
    ax.set_zticks([0, 127.5, 255])

    rs = []
    gs = []
    bs = []
    cs = []

    for row in range(height):
        for col in range(width):
            r, g, b = px[col, row]
            c = (r / 255, g / 255, b / 255)
            rs.append(r)
            gs.append(g)
            bs.append(b)
            cs.append(c)

    ax.scatter(rs, gs, bs, c = cs)
    if out:
        plt.savefig(out, dpi=300)
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='input image filepath')
    parser.add_argument('-o', '--out', help='output to file at specified path')
    args = parser.parse_args()

    image = Image.open(args.filepath)

    imgcolorplot(img=image, out=args.out)

if __name__ == '__main__':
    main()