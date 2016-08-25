import random, pathlib
# from sys import random
f = open('data.csv', 'w')
w, h = 256, 256

for y in range(h):
    for x in range(w):
        f.write(str(random.randrange(0, 255)) + ',')
    f.write('\n')

f.close()