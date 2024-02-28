import random
from dictionary import *


i1=random.randint(1,len(words2))
print("the number is %d" % i1)
theword=words2[i1]
length=len(theword)
# print("the length of the word is  %d" % length)
i2=[]
i2.append(random.randint(0,length-2))
i2.append(random.randint(i2[0]+1,length-1))

attempts=length*3
print("You have %d attempts" % attempts)
print (i2[0] * '* '+theword[i2[0]] +(i2[1] -i2[0] -1)*'* '+theword[i2[1]]+(length-i2[1]-1)*'* ')
guess=str(0)


while (not (guess.isalpha()  and len(guess)==1)  ):
    guess=input("Please insert a letter:     ")
    if (not guess.isalpha()):
        print("This is not a letter. Try again.")
    if (len(guess)>1):
        print("This is too long.give me a ONE single letter:    ")

attempts=attempts-1
theword.count(guess)
