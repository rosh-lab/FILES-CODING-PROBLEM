#Program which will display the content of any file by accepting the file name from keyboard..
#FileReadEx3.py
try:
    filename=input("Enter file name to view its content:")
    fp=open(filename,"r")
except FileNotFoundError:
    print("File does not exist")
else:
    filedata=fp.read()
    if(len(filedata)==0):
        print("File is empty")
    else:
        print("=================")
        print("Content of:{}".format(fp.name))
        print("================")
        print(filedata)
        print("================")
