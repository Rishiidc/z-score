import os
import shutil

path = input("Enter the name of the folder that you want to solve")
files = os.listdir(path)
print(files)
for file in files:
    name,extension = os.path.splitext(file)
    print(name,extension)
    if extension == '':
        continue

    if os.path.exists(path+'/'+extension):
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)

    else:
        os.makedirs(path+"/"+extension)
        shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
