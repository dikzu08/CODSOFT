import random

userWin = 0
ComputerWin = 0

game = ['rock', 'paper','sissor']

while True:
    

    userChoise = input("Choise You Take Rock/Paper/Sissor or Quit or Result : ").lower()
    if userChoise == "quit":
        print("----------Game Ended----------")
        break

    if userChoise == "result":
        print("User Win : " , userWin)
        print("Computer Win : ", ComputerWin)
        # if(userWin > ComputerWin):
        #     print("User Win Overall Game by"+ (userWin - ComputerWin) +"Number of Difference")

        # else:
        #     print("Computer Win Overall Game by"+ (-userWin + ComputerWin) +"Number of Difference")

        print("----------Game Ended----------")
        break

    if userChoise  not in game:
        print("Choise a valid Options ")
        continue

    randomChoise = random.randint(0,2)
    computerChoise = game[randomChoise]
    print("Computer Choise: ", computerChoise)

    if(computerChoise == userChoise):
        print('Its a Draw !!!')
        userWin = userWin  + 1
        ComputerWin = ComputerWin  + 1
        print ("Try Again.....")

    if (userChoise == "rock"and computerChoise == "sissor" ):
        print ("User Win!\n")
        userWin = userWin  + 1

    if (userChoise == "sissor"and computerChoise == "paper" ):
        print ("User Win!\n")
        userWin = userWin  + 1

    if (userChoise == "paper"and computerChoise == "rock" ):
        print ("User Win! \n")
        userWin = userWin  + 1


    if (userChoise == "rock"and computerChoise == "paper" ):
        print ("Computer Win!\n")
        ComputerWin = ComputerWin  + 1

    if (userChoise == "sissor"and computerChoise == "rock" ):
        print ("Computer Win!\n")
        ComputerWin = ComputerWin  + 1

    if (userChoise == "paper"and computerChoise == "sissor" ):
        print ("Computer Win!\n")
        ComputerWin = ComputerWin  + 1



