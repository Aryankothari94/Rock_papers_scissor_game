"""
rock = 1
paper = 0
secessor = -1"""
import random

yourscore = 0
compscore = 0
draw = 0
for i in range(10):
    computer = random.choice([1,-1,0])
    yourchoice = input("enter your choice:")
    yourdict={"r":1,"p":0,"s":-1}
    reversedict ={1:"rock", 0:"paper", -1:"scissor"}
    you =yourdict[yourchoice]


    if(you==1 and computer==0 or you==1 and computer==-1 or you==-1 and computer==0 ):
        print(f"your choice is: {reversedict[you]} \n computer  choice is: {reversedict[computer]} \n you will win this match")
        yourscore+=1

    elif(you==0  and  computer==-1 or you==0  and  computer==1 or you==-1  and  computer==1):
        print(f"your choice is: {reversedict[you]} \n computer  choice is: {reversedict[computer]} \n computer will win this match")
        compscore+=1

    elif(you==computer):
        print(f"your choice is: {reversedict[you]} \n computer  choice is: {reversedict[computer]} \n Its a draw match")
        draw+=1


if(yourscore>compscore):
    print(f"finally you are winner...you win {yourscore} matches out of 10")

elif(yourscore<compscore):
    print(f"finally computer are winner...computer win {compscore} matches out of 10")

elif(yourscore==computer):
    print(f"you both win {yourscore}-{compscore} matches")