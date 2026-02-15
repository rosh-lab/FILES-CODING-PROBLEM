#Program for demonstrating how to write the data to the file..
#FileWriteEx2.py
sno=120
sname="saif"
marks=30.45
with open("Stud.data","a") as fp: #Data will overlapped....
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data written to the file ..Go and check it")
