#Program for demonstrating how to write the data to the file..
#FileWriteEx3.py
sno=int(input("Enter your roll number:"))
sname=input("Enter your name:")
marks=float(input("Enter your marks:"))
with open("Stud.data","a") as fp: #Data will overlapped....
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\n")
    print("Data written to the file ..Go and check it")
