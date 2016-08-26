# First, install numpy and pillow on your system like this:
# Open terminal and type pip install numpy
# then, pip install pillow

from PIL import Image
import numpy as np
import csv

w, h = 59, 79
data = np.zeros((h, w), dtype=np.uint8)
# data = np.zeros((h, w), np.int)

with open('Flir_Image_of_me.csv', 'r') as f:
    for x, row in enumerate(csv.reader(f, dialect='excel', delimiter='\t')):
        row.pop(w) # remove \n
        for y, column in enumerate(row):
            try:
                data[x, y] = int(column)
            except ValueError:
                pass
            except IndexError:
                print("error")

    print(data)


img = Image.fromarray(data, 'L')
img.save('image.png')
img.show()