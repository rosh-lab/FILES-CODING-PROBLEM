#Program for reading employee values and save them as record in a file...
#EmpPickEx1.py
import pickle
with open("Emp.data","ab") as fp:
    while(True):
    #Accept the employees values from the keyboard
        print("==========================================")
        empno=int(input("Enter employee number:"))
        ename=input("Enter employee name:")
        sal=float(input("Enter employee salary:"))
        dsg=input("Enter employee designation:")
        print("=========================================")
        #create an empty list and place emp values
        lst=list() #Empty list created
        lst.append(empno)
        lst.append(ename)
        lst.append(sal)
        lst.append(dsg)
    #SAve or transfer lst data into the file
        pickle.dump(lst,fp)
        print("Employee Record saved in file successfully:")
        print("==================================================")
        ch=input("Do you want to enter another record?(Yes/No):)")
        if(ch.lower()=="no"):
            print("Thanks for using this program:")
            break