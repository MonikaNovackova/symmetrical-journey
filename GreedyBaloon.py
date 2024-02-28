import random
import time

def Intro():
    time.sleep(0.4)
    print("In each round I will ask you if you want me to blow the baloon more.")
    time.sleep(1.4)
    print("The bigger your baloon is, the better.")
    time.sleep(0.7)
    print("Remember two things:")
    time.sleep(0.6)
    print("1. If you try to blow the baloon over its capacity, it will crack")
    time.sleep(1.4)
    print("2. It is never certain how much additional air gets into baloon with each blow.")
    time.sleep(1.6)
    print("Let's start")






class Baloon:
    content=0
    capacity=10
    def blow(self):
        more=True
        print("The content is %d" % self.content)
        while more:
            answer="?"
            while ((not (answer =="y" or answer =="n")) and (not self.content> self.capacity)):
                answer=input("Blow more? y/n   ")
                if (answer == "n"):
                    print("Great. We are done. The size of your baloon is %d " % self.content)
                    more=False
            airVol=random.randint(1,6)
            self.content=self.content+airVol
            if (more and (self.content > self.capacity)):
                print(" BUUUUUUUM     CRAAAAAAAAAAAACK..Your baloon's gone!!")
                more=False    
            elif more:
                print("The new content is %d" % self.content)


