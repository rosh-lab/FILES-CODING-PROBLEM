#Write a python program which will accept the data dynamically from the keyboard and write it to the file
#DynamicFileWriteEx1.py
print("Enter the data from the keyboard Press @ to stop!")
with open("hyd.data","a") as fp:
    while(True):
        kbdata=input()
        if(kbdata!="@"):
            fp.write(kbdata+"\n")
        else:
            print("Data written to the file ----verified")
            break