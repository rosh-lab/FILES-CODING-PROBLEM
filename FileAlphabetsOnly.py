#Program which will accept any file name and display all the words which contains alphabets only..
#FileAlphabetsOnly.py
import string
try:
    filename=input("Enter any file name:")
    with open(filename,"r") as fp:
        data=fp.read() #read full file
        if (len(data) == 0):
            print("Empty file")
        else:
            words=data.split() #split into words
            for word in words:
                word=word.strip(string.punctuation) #Removes punctuation
                if(word.isalpha()): #check only alphabets
                    print(word)
except FileNotFoundError:
    print("File doesn't exist")

