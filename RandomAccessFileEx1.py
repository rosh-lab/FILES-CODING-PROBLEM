#Program for demonstrating how to access the data randomly from the file..
#RandomAccessFileEx1.py
#FilePointerObject.tell()===>>Gives index of file pointer
#Filepointer.seek(Index)====>>Will set file pointer to point to the specified index.
with open("Kvr1.data","r") as fp:
    print("Initially--FP points to:{}".format(fp.tell())) #0   HYD IS THE
    # #Capital of ts
    filedata=fp.read(3)
    print("File Data:",filedata)
    print("Now FP points to:{}".format(fp.tell()))
    filedata=fp.read(4)
    print("File Data:",filedata)
    print("Now FP points to:{}".format(fp.tell()))
    filedata=fp.read(3)
    print("File Data:",filedata)
    print("Now FP points to:{}".format(fp.tell())) #10
    filedata=fp.read(3)
    print("File Data:",filedata)
    print("Now FP points to:{}".format(fp.tell()))
    filedata = fp.read(5)
    print("File Data:", filedata)
    print("Now FP points to:{}".format(fp.tell()))
    #To reset the file Pointer,we use seek()
    fp.seek(7)
    print("Now FP points after seek() to {}:".format(fp.tell()))
    filedata=fp.read(3)
    print("File Data:",filedata)
    print("Now FP points to:{}".format(fp.tell()))
    fp.seek(0)
    print("Now FP points after seek() to :{}".format(fp.tell()))
    #REad complete data from file
    filedata=fp.read()
    print("File Data:",filedata)
    print("Now FP points after seek() to :{}".format(fp.tell()))