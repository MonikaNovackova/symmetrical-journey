import random
import time

def throw():
    return(random.randint(1,6))

def main():
    guessI=18

    print("You will guess an integer from 1 to 6. Then an integer number x between 1 and 6 will be generated.")
    time.sleep(1)
    print("If your guess turns out to be equal to x, you can ask me a question and I will answer truthfully.")
    time.sleep(1)
    print("If your guess is higher than the generated number, I will give you following number of rizzles: 10*(your guess - x). ")
    time.sleep(1)
    print("But If you guess is less than the generated number, you have to give me (10*(x-your guess) rizzles.")
    time.sleep(1)
    print("Pretty, good game, init? ")
    time.sleep(1)
    guess=input("Tell me your guess NOW! If you don't want to play, press 'q'. ")

    while (  (int(guessI)>6) or  (int(guessI)<1)  )  :
   
        if (guess == 'q'):
            exit('Bbyyyee')  

        try: 
            guessI=int(guess)

            if int(guessI) > 6:
                guess=input("Too big. ".upper() + "Try again:  ")
            elif int(guessI) < 1:
                print('Too small. '.upper())
                guess=input("Try again:  ")

        except ValueError:
            print("this is not an integer".upper())
            guess=input("Try again:  ")
    time.sleep(0.3)
    print("so, your guess is %d" % guessI)
    time.sleep(1)
    print("OK, lets roll the dice..")

    x=throw()
    time.sleep(1)
    print("the number is..")
    time.sleep(1)
    print("..%d !" %x)

    if guessI==x:
        print("Cool. You win. Ask me a question!")

    elif guessI>x:
   
        rzs=10*(guessI-x)
        print("Good for you. Here is your %d rizzles." % rzs)

    else:
        rzs=10*(x-guessI)
        print("Yep! Gimme %d rizzles." % rzs)
