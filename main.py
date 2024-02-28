import time

print("Hello. You can play with me.")
i="I am a quiter"
while (not i=="q"):
    time.sleep(0.8)
    print("I can play two games.")
    time.sleep(1)
    print("One is called 'DICE' and the other is called 'GREEDY BALOON'. ")
    time.sleep(1)
    i=input("For playing DICE press 'd'. For playing GREEDY BALOON press 'b'. To quite press'q'. ")

    if i=='d':
        print('good, lets play the dice!')
        from dice import main
        main()
        i=input("If you want to quit press 'q'. If you don't want to quit, press anything else. ")
    elif i=="b":
        print("Coel, baloon it is.")
        from GreedyBaloon import Intro, Baloon
        Intro()
        baloon1=Baloon()
        baloon1.blow()
        i=input("To quit pres 'q'. If you don't want to quit, press anything except 'q'. ")


if i =='q':
    exit('Bbyyyee')
