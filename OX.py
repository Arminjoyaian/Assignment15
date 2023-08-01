
import os

path = "/"

dir_list = os.listdir(path)

print("Files directories in '", path, "' :")

try:
    f = open('test.txt','r')
except OSError:
    print('Catched OSError in except block')


os.access('test.txt',os.F_OK)
os.access('test.txt',os.R_OK)
os.access('test.txt',os.W_OK)
os.access('test.txt',os.X_OK)