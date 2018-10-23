import random
message1 = "player1 wins"
message2 = "player2 wins"

game = True
while game == True:
    def dice_roll():
        empty1 = []
        empty2 = []
        player1 = ([random.randint(1,6)for i in range (10)])
        player2 = ([random.randint(1,6)for i in range (10)])
        if sum(player1) > sum(player2):
            print(str ("Player1 is the victor: " + str(sum(player1))))
        else:
            print("Player2 is the victor: " + str(sum(player1)))

    dice_roll()

    noanswer = True
    while noanswer:
        answer = input("Do you wish to roll again? Y or N")
        if answer == "Y":
            noanswer = False
            print ("Once more")
        elif answer == "N":
            noanswer == False
            game = False
            print ("Farewell and to all goodnight")
            quit()
        else:
            print("you must answer Y or N")
            


               
