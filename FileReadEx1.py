#Program for reading the data from the file..
#FileReadEx1.py
try:
    with open("hyd.data") as fp:
        filedata = fp.read()
        print("============================")
        print(filedata)
        print(type(filedata))
        print("==============================")
except FileNotFoundError:
    print("File does not exist")