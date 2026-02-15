#write a python program which will copy the content of one file into another file
#FileCopyEx1.py
try:
    srcfile=input("Enter Source file:")
    with open(srcfile,"rt") as rp: #Opening the Src file in read mode #Here r is a mode and t is text file
        dstfile=input("Enter Destination file:")
        with open(dstfile,"at") as wp:#Opening the Dest file in write mode #a is mode and t is text file
            srcdata=rp.read() #Read the data from the SRC file
            wp.write(srcdata) #Writing the Src file data to Dest file
            print("File copied successfully")
except FileNotFoundError:
    print("Source file does not exist")
