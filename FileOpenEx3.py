#This program demonstrate how to open the file..
#FileOpenEx3.py
try:
    with open("Kvr1.data") as fp:
        print("type of fp=",type(fp))
        print("File opened in read mode successfully")
except FileNotFoundError:
    print("File does not exist")