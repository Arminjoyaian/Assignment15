import os
import imageio

IMAGES = []

for name in sorted(os.listdir("img")):
    IMAGES.append(imageio.imread("img/" + name))

imageio.mimsave("out.gif",IMAGES)