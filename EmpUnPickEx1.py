#Program for reading the records from the file(emp.data) where it contains employee records..
#EmpUnPickEx1.py
import pickle
with open("Emp.data","rb") as fp:
    print("================================")
    while (True):
        try:
            record=pickle.load(fp)
            for val in record:
                print("{}".format(val),end="\t")
            print()
        except EOFError:
            print("***********************************************")
            break
