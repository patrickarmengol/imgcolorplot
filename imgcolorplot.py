# visualize an rgb color space box of an image
# TODO: take commandline args, exception handling, save plot to image

import matplotlib.pyplot as plt
from PIL import Image


def imgcolorplot(filepath):
    im = Image.open(filepath)

    px = im.load()
    width, height = im.size

    ax = plt.axes(projection = '3d')

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
    plt.show()


def main():
    filepath = 'hydeoutproductions.jpg'

    imgcolorplot()

if __name__ == '__main__':
    main()