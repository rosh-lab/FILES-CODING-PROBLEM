#Program for copying the image....
#ImageFileCopy.py
try:
    with open("C:\\Users\\rosha\\Files(Creating Practice)\\Eye.jpg","rb") as rp:  #Here r is a mode and b is binary file
        with open("pyt.jpg","wb") as wp: #w is mode and b is binary file
            srcdata=rp.read()
            wp.write(srcdata)
            print("Image File copied successfully")
except FileNotFoundError:
    print("Source file does not exist")

