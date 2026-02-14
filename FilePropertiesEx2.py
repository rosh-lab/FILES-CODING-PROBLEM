#Program for Demonstrating obtaining the file properties
#FilePropertiesEx2.py
try:
    fp=open("Kvr2.data")
except FileNotFoundError:
    print("File does not exist")
else:
    print("======================================")
    print("File opened in read mode successfully")
    print("Name of the file=",fp.name) #Name is an attribute of file pointer(fp) object.
    print("File Mode=",fp.mode) #Mode is an attribute of file pointer(fp) obbject
    print("Is this file readable?=",fp.readable()) #Here readable() is an function
    print("Is this file writable?=",fp.writable()) #Here writeable() is an function
    print("Is this file is closed?=",fp.closed) #Here closed is an attribute..
    print("======================================")
    print("Out off with open()as ======Is this closed?",fp.closed) #Here no concept of autocloseability is applied...
finally:
    print("I am from finally block")
    fp.close() #Manual closing this is.....
    print("Is this file closed now?=",fp.closed) #Yes now it is closed only..