import random
#-------------------------------------------------------------------------------
# Name:        snake water gun game
# Purpose:
#
# Author:      karan
#
# Created:     03/03/2022
# Copyright:   (c) karan 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def results(comp,player):
    if (player.capitalize()=="S" or player.capitalize()=="W" or player.capitalize()=="G"):
        #if two values are equal, declare a tie
        if player.capitalize()==comp:
            print("match draw")
        #all possiblities of player's win
        elif (player.capitalize()=="S" and comp=="W") or (player.capitalize()=="W" and comp=="G") or (player.capitalize()=="G" and comp=="W"):
            print("you won")
        # all rmaining possibilities
        else:
            print("you loose")
    # printing an error if player presses wrong key
    else:
        print("invalid selection")
#randomly selecting values for computer
randno=random.randrange(1,3)
if randno==1:
    comp="S"
elif randno==2:
    comp="W"
else:
    comp="G"
#prompt for user to choose a "g","w","s"
player=input("press (s) to choose snake\n press (w) to choose water \n press (g) to choose gun \n")
#printing results from computer selection
print(f"computer chose {comp}")
results(comp,player)


