# First, install numpy and pillow on your system like this:
# Open terminal and type pip install numpy
# then, pip install pillow

from PIL import Image
import numpy as np
import csv

w, h = 256, 256
data = np.zeros((h, w), dtype=np.uint8)
# data = np.zeros((h, w), np.int)

with open('data.csv', 'r') as f:
    #my_list = [[int(x) for x in rec] for rec in csv.reader(f, dialect='excel', delimiter=',')]

    for x, row in enumerate(csv.reader(f, dialect='excel', delimiter=',')):
        row.pop(w) # remove \n
        for y, column in enumerate(row):
            try:
                data[x, y] = int(column)
            except ValueError:
                pass

    print(data)


img = Image.fromarray(data, 'L')
img.save('my.png')
img.show()