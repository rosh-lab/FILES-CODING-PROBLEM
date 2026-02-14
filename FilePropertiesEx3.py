#Program for Demonstrating obtaining the file properties
#FilePropertiesEx3.py
with open("C:\\Users\\rosha\\Files(Creating Practice)\\Kvr3.data","a") as fp:
    print("======================================")
    print("Name of the file=",fp.name) #Name is an attribute of file pointer(fp) object.
    print("File Mode=",fp.mode) #Mode is an attribute of file pointer(fp) obbject
    print("Is this file readable?=",fp.readable()) #Here readable() is an function
    print("Is this file writable?=",fp.writable()) #Here writeable() is an function
    print("Is this file is closed?=",fp.closed) #Here closed is an attribute..
    print("======================================")
print("Out off with open()as ======Is this closed?",fp.closed)