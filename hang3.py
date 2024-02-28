import random
from dictionary import *

def CheckLetter(aword,aletter):
    return [counter for counter, value in enumerate(aword) if (value==aletter)]


#------------------------------------------------------------------------------------------------------------------------------------------------------
i1=random.randint(1,len(words2))

theword=words2[i1]
length=len(theword)
print(theword)
wordguessed=length* '* '
print(wordguessed)

i2=[]
i2.append(random.randint(0,length-2))
i2.append(random.randint(i2[0]+1,length-1))
print(i2)
attempts=length*3

listch=[]

for counter,value in enumerate(wordguessed):
    if counter == (i2[0]):
        listch.append(theword[i2[0]])
    else:
        listch.append(value)

print(listch)
print("".join(listch))


print("You have %d attempts" % attempts)
print (i2[0] * '* '+theword[i2[0]] +(i2[1] -i2[0] -1)*'* '+theword[i2[1]]+(length-i2[1]-1)*'* ')


while (attempts>0):
    guess=str(0)
    while (not (guess.isalpha()  and len(guess)==1 and guess=="Q"  )):
        guess=input("For exit press Q. Otherwise please insert a letter:     ")
        if (not guess.isalpha()):
            print("This is not a letter. Try again.")
        if (len(guess)>1):
            print("This is too long.give me a ONE single letter:    ")
        if guess =='Q':
            exit('Bbyyyee')

    if theword.count(guess)>0:
        hitIndecies=CheckLetter(theword,guess)




attempts=attempts-1

theword.count(guess)
