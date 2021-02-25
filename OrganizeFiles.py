import shutil
import os

path = input("Enter The name Of Directory to be sorted")

listOfFiles=os.listdir(path)

for file in listOfFiles :
    name,ext=os.path.splitext(file)
    if(ext==""):
        continue
    if(os.path.exists(path+"/"+ext)):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
