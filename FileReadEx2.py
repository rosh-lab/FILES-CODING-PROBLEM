#Program for reading the data from the file..
#FileReadEx2.py
try:
    with open("hyd.data") as fp:
        filedata = fp.readlines()
        print("============================")
        print(type(filedata))
        for line in filedata:
            print(line,end="")
        print("==============================")
except FileNotFoundError:
    print("File does not exist")