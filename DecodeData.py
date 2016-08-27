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




# # Another method, found here: http://designalyze.com/intro-scripting-python-rhino/intro-python-scripting-16-import-points-csv

# #Import Points from CSV

# import rhinoscriptsyntax as rs

# #Select a file to open
# filename = rs.OpenFileName("Open CSV file","*.csv|", None, None, None)

# #open the file for reading
# file = open(filename, 'r')

# lines = file.readlines()

# file.close()

# #delete the first line because it's a header
# del lines[0]
# #print to check the data
# print(lines)

# ptNumber = 0

# for line in lines:
#     #remove the \n
#     line = line.strip()
#     #split the line by the comma
#     ptInfo = line.split(',')
#     x = float(ptInfo[0])
#     y = float(ptInfo[1])
#     z = float(ptInfo[2])
#     r = int(ptInfo[3])
#     g = int(ptInfo[4])
#     b = int(ptInfo[5])
#     pt = rs.AddPoint(x,y,z)
#     color = (r,g,b)
#     rs.ObjectColor(pt, color)
#     name = "pt_" + str(ptNumber)
#     rs.ObjectName(pt,name)
#     ptNumber += 1
