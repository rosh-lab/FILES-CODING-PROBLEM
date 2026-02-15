#Program for demonstrating hhow to write the iterable object data to the file
#FileWriteEx4.py
x={100:"Travis",200:"Numpy",300:"Pandas",400:"Arjun"}
with open("Stud1.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data written to the file")