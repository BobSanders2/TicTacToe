import re
from random import *
from time import *
from AI import Ai

class TicTacToe:
    def __init__(self):
        self.setchar = ""
        self.compchar = ""
        self.compstart = []

        self.gamestarted = False
        self.quit = False

        matrix = ["", "", "", "", "", "", "", "", ""]
        self.gamematrix = ["", "", "", "", "", "", "", "", ""]
        self.openspaces = [i for i, e in enumerate(self.gamematrix) if e == ""]
        self.board = f"""

           A    B    C
        1  {self.gamematrix[0]} |  {self.gamematrix[1]}  | {self.gamematrix[2]}
          -------------
        2  {self.gamematrix[3]} |  {self.gamematrix[4]}  | {self.gamematrix[5]}
          -------------
        3  {self.gamematrix[6]} |  {self.gamematrix[7]}  | {self.gamematrix[8]}
        """

    def rungame(self):
        self.initialsettings()
        while self.quit != True:
            self.checkboard(self.playerchar)
            print(self.board)
            self.getinput(self.playerchar)
            if self.checkboard(self.playerchar) == self.playerchar:
                print(self.board)
                print("You Won!\n")
                print("Congrats!")
                break
            elif self.checkboard(self.playerchar) == "Tie":
                print(self.board)
                print("It's a tie\n")
                print("Try again!")
                break
            else:
                pass
            print(self.board)
            self.compspeak()
            computerturn = self.computerturn()
            self.gamematrix = computerturn[0]
            self.compstart = computerturn[1]
            if self.checkboard(self.compchar) == self.compchar:
                print(self.board)
                print("You Lose!\n")
                print("You're a loser! Congrats!")
                break
            elif self.checkboard(self.playerchar) == "Tie":
                print(self.board)
                print("It's a tie\n")
                print("Try again?")
                yesno = input(">>>")
                no = False
                while no == False:
                    if yesno.upper() == "YES":
                        TicTacToe.rungame()
                    elif yesno.upper() == "NO":
                        break
                    else:
                        print("That isn't a valid option.")
            else:
                pass

    def initialsettings(self):
        if self.gamestarted == False:
            print("Please Select Either 'X' or 'O'")
            char = input(">>>")
            if char.upper() == "X":
                self.playerchar = "X"
                self.compchar = "O"
                self.compstart = sample(self.openspaces, 1)
            else:
                self.playerchar = "O"
                self.compchar = "X"
                self.gamestarted = True
                self.compspeak()
                self.gamematrix[randint(0, 9)] = "X"
                self.compstart = [i for i, e in enumerate(self.gamematrix) if e == "X"]
        else:
            pass

    def getinput(self, char):
        dictionary = {"A1": 0, "B1": 1, "C1": 2, "A2": 3, "B2": 4, "C2": 5, "A3": 6, "B3": 7, "C3": 8}
        move = ""

        while move.upper() != "QUIT":
            print(f"Where do you want to put your {char}? i.e. A2")
            move = input(">>>")

            if move.upper() == "QUIT":
                self.quit = True
                break
            elif move.upper() in dictionary:
                x = dictionary[move.upper()]
                coords = [x]
                self.markboard(coords, char)
                break
            else:
                print("\nThat is not a valid value. Please try again.\n")

    def computerturn(self):
        self.setcurrentboard()
        gamedetails = Ai(gamematrix=self.gamematrix, compchar=self.compchar, compstart=self.compstart, playchar=self.playerchar).move()
        return gamedetails
    def compspeak(self):
        phrases = ["I hope this works!", "Wow, this is hard.", "I think if I do this I can win.", "Am I winning?", "Hmm, I think I have you now!"]
        print("""


                        Computer will move.


                        """)
        print("Thinking", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".")
        sleep(3)
        phr = sample(phrases, 1)
        print(f"""


                                {phr[0]}


                                """)
        sleep(2)

    def markboard(self, coordinates, char):
        self.gamematrix[coordinates[0]] = char

    def setcurrentboard(self):
        self.board = f"""

           A    B    C
        1  {self.gamematrix[0]} |  {self.gamematrix[1]}  | {self.gamematrix[2]}
          -------------
        2  {self.gamematrix[3]} |  {self.gamematrix[4]}  | {self.gamematrix[5]}
          -------------
        3  {self.gamematrix[6]} |  {self.gamematrix[7]}  | {self.gamematrix[8]}
                """

        self.openspaces = [i for i, e in enumerate(self.gamematrix) if e == ""]

    def checkboard(self, char):
        self.setcurrentboard()

        if self.gamematrix[0] == char and self.gamematrix[1] == char and self.gamematrix[2] == char:
            return char
        elif self.gamematrix[3] == char and self.gamematrix[4] == char and self.gamematrix[5] == char:
            return char
        elif self.gamematrix[6] == char and self.gamematrix[7] == char and self.gamematrix[8] == char:
            return char
        elif self.gamematrix[0] == char and self.gamematrix[3] == char and self.gamematrix[6] == char:
            return char
        elif self.gamematrix[1] == char and self.gamematrix[4] == char and self.gamematrix[7] == char:
            return char
        elif self.gamematrix[2] == char and self.gamematrix[5] == char and self.gamematrix[8] == char:
            return char
        elif self.gamematrix[0] == char and self.gamematrix[4] == char and self.gamematrix[8] == char:
            return char
        elif self.gamematrix[2] == char and self.gamematrix[4] == char and self.gamematrix[6] == char:
            return char
        elif self.openspaces == []:
            return "Tie"
        else:
            return None



TicTacToe().rungame()