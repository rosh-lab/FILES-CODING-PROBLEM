#This program demonstrate how to open the file..
#FileOpenEx1.py
try:
    fp=open("Kvr1.data","r") #"r" mode read the data only
    print("type of fp=",type(fp))
    print("File opened in read mode successfully..")
except FileNotFoundError:
    print("File does not exist")