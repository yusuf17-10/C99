import shutil
import os

source=input("Enter The name Of source Directory :  ")
destination=input("Enter The name Of Destination Directory :  ")

source = source+"/"
destination=destination+"/"

listOfFiles=os.listdir(source)

for file in listOfFiles :
    shutil.copy(source+file,destination)
