from EmpPickEx2 import saverecord
from EmpPickUnPickMenu import menu
from EmpUnPickEx2 import readrecord
while True:
    try:
        menu()
        ch=int(input("Enter your choice: "))
        match(ch):
            case 1:
                saverecord()
            case 2:
                readrecord()
            case 3:
                print("Thanks for using this program")
                break
            case _:
                print("Your selection of operation is wrong --try again")
    except ValueError:
        print("Don't enter alnums,strs,floats and symbols for choice of operation----enter int values.")