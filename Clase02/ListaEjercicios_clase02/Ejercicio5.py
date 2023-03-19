
import os
path=os.path.abspath('..')
for f in os.scandir(path):
    print(f,"=>",f.path)
    print(f.is_dir())
def funcionRecursiva(path):
    #funcion que me liste el path
    listaCarpeta=[]
    for f in listaCarpeta:
        if f.isDir():
            funcionRecursiva(f.path)
        else:
            print(f.path)