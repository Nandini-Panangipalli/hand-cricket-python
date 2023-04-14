# Instructions
 
print(""" -------- Game of Cricket --------
 
Instructions to follow:
 
1. You have to select any random number from 1 to 10.
2. Next the computer will also select a number.
3. While your batting, if the number selected by you and computer is different, then your number will add to your runs.
   If the number selected by you and computer is same, then you will lose one wicket.
4. While your bowling, if the number selected by you and computer is different, then the computer's number will add to its runs.
   If the number selected by you and computer is same, then the computer will lose one wicket just like the previous rule.
5. You and the computer get 2 wickets and 2 overs for batting and bowling.
6. Here each over consists of 6 balls which is for two overs players get to bowl 12 balls in total.
7. The innings will end after either of the 2 wickets fall or the overs end.
8. The player with maximum runs wins. """)
 
print("\n---------- Start Game ----------")
 
#importing random to get random input from the computer

import random
 
# Toss Time 
 
print("\n It's time for the Toss")
toss = (input("Choose heads or tails: ")).lower() #in lowercase
 
rand_toss = random.randint(1,2)            # In rand_toss (1 = Heads) and (2 = Tails) ------rand=random
rand_opt = random.randint(1,2)             # In rand_opt (1 = bat) and (2 = ball)
 
your_opt = 0          #your option that you chose
comp_opt = 0         #computer's option
 
#if-else to know if we won the toss and to choose bat or ball if we win the toss

if rand_toss == 1 and toss == "heads":
    print("\nCongratulations!You have won the toss...")
    your_opt = (input("Now choose to bat or ball: ")).lower()
 
elif rand_toss == 2 and toss == "tails":
    print("\nYou won the toss")
    your_opt = (input("Choose bat or ball: ")).lower()    
  
else:
    print("\nSorry!You have lost the toss...")
 
 #computers option once the you lost the toss 
    if rand_opt == 1:
        comp_opt = "bat"
        print("Computer choose to bat")
        print("Now you have to ball!...All the best!")
 
    elif rand_opt == 2:
        comp_opt = "ball"
        print("Computer choose to ball")
        print("You have to bat!...All the best!")
 
# First Innings 
 
print("\n---------- First Innings Begins ----------")

runs_p1 = 0                       #Runs of the first player batting
wickets_p1 = 0                    #Wickets fallen down of the first team
balls_p1 = 0                      #balls starting from 1 to 12
 
while (wickets_p1 != 2 and balls_p1 != 12):
 
    your_choice = int(input("\nChoose any number from 1 to 10: "))
    comp_choice = random.randint(1,10)
 
    if (your_choice < 1 or your_choice > 10):
        print("\nPlease choose a value only from 1 to 10.")
 
    else:
        print("Your choice: ",your_choice,"\nComputer's choice: ",comp_choice)
 
        if (your_choice == comp_choice):
            wickets_p1 += 1                  #incrementing the wickets as the number is same a wicket has fallen down
 
        else:
            if (your_opt == "bat" or comp_opt == "ball"):
                Bat_first = "You"
                Ball_first = "Computer"
                runs_p1 += your_choice           #Incrementing runs of the first player
 
            elif your_opt == "ball" or comp_opt == "bat":
                Bat_first = "Computer"
                Ball_first = "You"
                runs_p1 += comp_choice   #Incrementing runs of the computer
 
        print("\nScore =",runs_p1,"/",wickets_p1)
 
        balls_p1 += 1  #Incrementing the balls
 
        if (balls_p1 == 6):
            print("End of Over 1")
 
        elif (balls_p1 == 12):
            print("End of Over 2")
 
        print("Balls remaining: ",12 - balls_p1)
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_p1)
print("wickets =",wickets_p1)
print("Balls played",balls_p1)
 
print("\n",Ball_first,"needs",runs_p1 + 1,"runs to win.")
 
# Second Innings  same as the first innings
 
print("\n---------- Second Innings Begins ----------")
 
runs_p2 = 0
wickets_p2 = 0
balls_p2 = 0
 
while (wickets_p2 != 2 and balls_p2 != 12 and runs_p2 <= runs_p1):
 
    your_choice = int(input("\nChoose any number from 1 to 10: "))
    comp_choice = random.randint(1,10)
 
    if (your_choice < 1 or your_choice > 10):
        print("\nPlease choose a value only between 1 to 10.")
 
    else:
        print("Your choice: ",your_choice,"\nComputer's choice: ",comp_choice)
 
        if (your_choice == comp_choice):
            wickets_p2 += 1
 
        else:
            if Bat_first == "Computer": 
                runs_p2 += your_choice
                Bat_second = "You"
 
            elif Bat_first == "You":
                runs_p2 += comp_choice
                Bat_second = "Computer"
 
        print("\nScore =",runs_p2,"/",wickets_p2)
 
        balls_p2 += 1
 
        if (balls_p2 == 6):
            print("End of Over 1")
 
        elif (balls_p2 == 12):
            print("End of Over 2")
 
        if (runs_p2 <= runs_p1 and balls_p2 <= 11 and wickets_p2 != 2):
            print("To win:",runs_p1 - runs_p2 + 1,"runs needed from",12 - balls_p2,"balls.")
 
print("\n---------- End of Innings ----------") 
 
print("\nFinal Score:")
print("Runs =",runs_p2)
print("wickets =",wickets_p2)
 
# Result of Match 
 
print("\n------- Result -------")
 
if (runs_p1 > runs_p2):
 
    if Bat_first == "You": 
        print("\nCongratulations! You won the Match by",runs_p1 - runs_p2,"runs.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",runs_p1 - runs_p2,"runs.") 
 
elif runs_p2 > runs_p1:
 
    if Bat_second == "You": 
        print("\nCongratulations! You won the Match by",wicket_p1 - wickets_p2,"wickets.")
 
    else:
        print("\nBetter luck next time! The Computer won the Match by",wickets_p1 - wickets_p2,"wickets.")
 
else:
    print("The Match is a Tie.","\nNo one Wins.")
              
print("See you again byeee...")