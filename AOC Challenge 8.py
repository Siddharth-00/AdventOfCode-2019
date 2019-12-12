import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
file = open("input.txt","r")
pixels = file.readline()
image = []
def compare(img, lay):
    if(img != '2'):
        return img
    else:
        return lay
for i in range(6):
    image.append([])
    for j in range(25):
        image[i].append('2')
for i in range(len(pixels)//150):
    layer = pixels[i * 150: i * 150 + 150]
    for j in range(len(layer)):
        image[j//25][j%25] = compare(image[j//25][j%25], layer[j])
print(image)
out = []
for i in range(6):
    for j in range(25):
        if(image[i][j] == '0'):
            out.append(1)
        else:
            out.append(0)
print(out)
plt.imsave('image.png', np.array(out).reshape(6,25), cmap=cm.gray)


    
