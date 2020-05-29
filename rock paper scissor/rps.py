import random    #for randint function	
import time      #for sleep function

print("\n\n\t\t\t Hello & Welcome to the game---- ROCK , PAPER and SCISSORS")
time.sleep(2)           #two sec delay

def print_value(choice):               #function to print value
	val={1:"ROCK",2:"PAPER",3:"SCISSORS"}   # values stored in dictionary
	time.sleep(0.5)	
	print(val[choice])

def usr_choice():       #function to input user choice
	statement="""\n 
	1 - ROCK
	2 - PAPER
	3 - SCISSORS
	enter your choice (1/2/3) - """
	print(statement)
	input_choice=input()
	try:                      #try block to try if user enters non int value
		choice=int(input_choice)
	except:
		print("\n\t\t!! invalid choice\n\tPlease enter valid choice")
		return(usr_choice())
	if(choice!=1 and choice!=2 and choice!=3):    #if else block to check value is 1/2/3
		print("\n\t\t!! invalid choice\n\tPlease enter valid choice")
		return(usr_choice())
	else:                                       
		print("your choice is - ")
		print_value(choice)
		return(choice)

def comp_choice():            #function to generate computer's choice
	choice=random.randint(1,3)
	print("computers choice is - ")
	print_value(choice)
	return(choice)

def result():            #function to calculate result
	usr=usr_choice()
	time.sleep(1)
	comp=comp_choice()
	time.sleep(1)
	value=usr-comp                
	if(value==0):
		print("\n\tITS A TIE !!")
		return(0)
	elif(value==-1 or value == 2):
		print("\n\tCOMPUTER WON !!")
		return(1)
	else:
		print("\n\tYOU WON !!")
		return(2)

play="yes"
comp=0
usr=0
while(play=="yes"):              #loop for rematch
	score=result()           #score, comp, usr variable to save the scores so far
	
	if(score==1):
		comp+=1
	elif(score==2):
		usr+=1
	time.sleep(1)
	print("\nSCORE - \n\tCOMPUTER = "+str(comp)+"\n\tYOU = "+str(usr))
	time.sleep(1.5)
	print("\nDo you want to play again ? (yes/no)")
	play=input()
