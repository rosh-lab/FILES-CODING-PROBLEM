#Program which will accept any file name and count number of lines,number of words and number of characters
#FileCountInfo.py
def filecountinfo():
    try:
        filename=input("Enter any file name:")
        with open(filename,"rt") as fp:
            nol=0 #Initial number of lines is equal to 0
            now=0 #Initial number of words=0
            noc=0 #Initially number of characters=0
            lines=fp.readlines()
            #print("Number of lines=",len(filedata)) this is through len but i want to go for coding technique..
            for line in lines:
                nol+=1
                now=now+len(line.split())
                noc=noc+len(line)
            else:
                print("==========================")
                print("Number of lines=",nol)
                print("Number of words=",now)
                print("Number of characters=",noc)
                print("==========================")
    except FileNotFoundError:
        print("File does not exist")
#Main program
filecountinfo()