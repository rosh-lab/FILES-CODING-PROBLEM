#Program for demonstrating how to write the data to the file..
#FileWriteEx1.py
sno=20
sname="Roshan"
marks=27.36
with open("Stud.data","w") as fp: #Data will overlapped....
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data written to the file ..Go and check it")
