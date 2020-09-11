import random

class Ai:
    def __init__(self, gamematrix, compchar, compstart, playchar):
        self.compstart = compstart
        self.gamematrix = gamematrix
        self.compchar = compchar
        self.playchar = playchar
        self.emptyspots = [i for i, e in enumerate(self.gamematrix) if e == ""]

    def move(self):
        if self.checkblock():
            self.blockmove()
        else:
            self.thirdmove()
            self.secondmove()
        return self.gamematrix, self.compstart

    def thirdmove(self):
        if self.compstart[0] == 0 and self.gamematrix[1] == self.compchar and self.gamematrix[2] == "":
            self.gamematrix[2] = self.compchar
        elif self.compstart[0] == 0 and self.gamematrix[1] == "" and self.gamematrix[2] == self.compchar:
            self.gamematrix[1] = self.compchar
        elif self.compstart[0] == 1 and self.gamematrix[0] == self.compchar and self.gamematrix[2] == "":
            self.gamematrix[2] = self.compchar
        elif self.compstart[0] == 1 and self.gamematrix[0] == "" and self.gamematrix[2] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[0] == self.compchar and self.gamematrix[1] == "":
            self.gamematrix[1] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[0] == "" and self.gamematrix[1] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 3 and self.gamematrix[4] == self.compchar and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
        elif self.compstart[0] == 3 and self.gamematrix[4] == "" and self.gamematrix[5] == self.compchar:
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[3] == self.compchar and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[3] == "" and self.gamematrix[5] == self.compchar:
            self.gamematrix[3] = self.compchar
        elif self.compstart[0] == 5 and self.gamematrix[3] == self.compchar and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 5 and self.gamematrix[3] == "" and self.gamematrix[4] == self.compchar:
            self.gamematrix[3] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[7] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[7] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[7] = self.compchar
        elif self.compstart[0] == 7 and self.gamematrix[6] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 7 and self.gamematrix[6] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[6] == self.compchar and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[6] == "" and self.gamematrix[7] == self.compchar:
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 0 and self.gamematrix[3] == self.compchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 0 and self.gamematrix[3] == "" and self.gamematrix[6] == self.compchar:
            self.gamematrix[3] = self.compchar
        elif self.compstart[0] == 3 and self.gamematrix[0] == self.compchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 3 and self.gamematrix[0] == "" and self.gamematrix[6] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[0] == self.compchar and self.gamematrix[3] == "":
            self.gamematrix[3] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[0] == "" and self.gamematrix[3] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 1 and self.gamematrix[4] == self.compchar and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
        elif self.compstart[0] == 1 and self.gamematrix[4] == "" and self.gamematrix[7] == self.compchar:
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[1] == self.compchar and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[1] == "" and self.gamematrix[7] == self.compchar:
            self.gamematrix[1] = self.compchar
        elif self.compstart[0] == 7 and self.gamematrix[1] == self.compchar and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 7 and self.gamematrix[1] == "" and self.gamematrix[4] == self.compchar:
            self.gamematrix[1] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[5] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[5] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[5] = self.compchar
        elif self.compstart[0] == 5 and self.gamematrix[2] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 5 and self.gamematrix[2] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[2] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[2] == self.compchar and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[2] == "" and self.gamematrix[5] == self.compchar:
            self.gamematrix[2] = self.compchar
        elif self.compstart[0] == 0 and self.gamematrix[4] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 0 and self.gamematrix[4] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[0] == self.compchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[0] == "" and self.gamematrix[8] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[0] == self.compchar and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 8 and self.gamematrix[0] == "" and self.gamematrix[4] == self.compchar:
            self.gamematrix[0] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[4] == self.compchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 2 and self.gamematrix[4] == "" and self.gamematrix[6] == self.compchar:
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[2] == self.compchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
        elif self.compstart[0] == 4 and self.gamematrix[2] == "" and self.gamematrix[6] == self.compchar:
            self.gamematrix[2] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[2] == self.compchar and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
        elif self.compstart[0] == 6 and self.gamematrix[2] == "" and self.gamematrix[4] == self.compchar:
            self.gamematrix[2] = self.compchar
        else:
            pass

    def blockmove(self):
        if self.gamematrix[0] == self.playchar and self.gamematrix[1] == self.playchar and self.gamematrix[2] == "":
            self.gamematrix[2] = self.compchar
            self.compstart[0] = 2
        elif self.gamematrix[0] == self.playchar and self.gamematrix[1] == "" and self.gamematrix[2] == self.playchar:
            self.gamematrix[1] = self.compchar
            self.compstart[0] = 1
        elif self.gamematrix[0] == "" and self.gamematrix[1] == self.playchar and self.gamematrix[2] == self.playchar:
            self.gamematrix[0] = self.compchar
            self.compstart[0] = 0
        elif self.gamematrix[3] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.gamematrix[3] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[5] == self.playchar:
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.gamematrix[3] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[5] == self.playchar:
            self.gamematrix[3] = self.compchar
            self.compstart[0] = 3
        elif self.gamematrix[6] == self.playchar and self.gamematrix[7] == self.playchar and self.gamematrix[8] == "":
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.gamematrix[6] == self.playchar and self.gamematrix[7] == "" and self.gamematrix[8] == self.playchar:
            self.gamematrix[7] = self.compchar
            self.compstart[0] = 7
        elif self.gamematrix[6] == "" and self.gamematrix[7] == self.playchar and self.gamematrix[8] == self.playchar:
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.gamematrix[0] == self.playchar and self.gamematrix[3] == self.playchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.gamematrix[0] == self.playchar and self.gamematrix[3] == "" and self.gamematrix[6] == self.playchar:
            self.gamematrix[3] = self.compchar
            self.compstart[0] = 3
        elif self.gamematrix[0] == "" and self.gamematrix[3] == self.playchar and self.gamematrix[6] == self.playchar:
            self.gamematrix[0] = self.compchar
            self.compstart[0] = 0
        elif self.gamematrix[1] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
            self.compstart[0] = 7
        elif self.gamematrix[1] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[7] == self.playchar:
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.gamematrix[1] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[7] == self.playchar:
            self.gamematrix[1] = self.compchar
            self.compstart[0] = 1
        elif self.gamematrix[2] == self.playchar and self.gamematrix[5] == self.playchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.gamematrix[2] == self.playchar and self.gamematrix[5] == "" and self.gamematrix[8] == self.playchar:
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.gamematrix[2] == "" and self.gamematrix[5] == self.playchar and self.gamematrix[8] == self.playchar:
            self.gamematrix[2] = self.compchar
            self.compstart[0] = 2
        elif self.gamematrix[0] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.gamematrix[0] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[8] == self.playchar:
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.gamematrix[0] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[8] == self.playchar:
            self.gamematrix[0] = self.compchar
            self.compstart[0] = 0
        elif self.gamematrix[2] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.gamematrix[2] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[6] == self.playchar:
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.gamematrix[2] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[6] == self.playchar:
            self.gamematrix[2] = self.compchar
            self.compstart[0] = 2
        else:
            return None


    def checkblock(self):
        if self.gamematrix[0] == self.playchar and self.gamematrix[1] == self.playchar and self.gamematrix[2] == "":
            return True
        elif self.gamematrix[0] == self.playchar and self.gamematrix[1] == "" and self.gamematrix[2] == self.playchar:
            return True
        elif self.gamematrix[0] == "" and self.gamematrix[1] == self.playchar and self.gamematrix[2] == self.playchar:
            return True
        elif self.gamematrix[3] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[5] == "":
            return True
        elif self.gamematrix[3] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[5] == self.playchar:
            return True
        elif self.gamematrix[3] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[5] == self.playchar:
            return True
        elif self.gamematrix[6] == self.playchar and self.gamematrix[7] == self.playchar and self.gamematrix[8] == "":
            return True
        elif self.gamematrix[6] == self.playchar and self.gamematrix[7] == "" and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[6] == "" and self.gamematrix[7] == self.playchar and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[0] == self.playchar and self.gamematrix[3] == self.playchar and self.gamematrix[6] == "":
            return True
        elif self.gamematrix[0] == self.playchar and self.gamematrix[3] == "" and self.gamematrix[6] == self.playchar:
            return True
        elif self.gamematrix[0] == "" and self.gamematrix[3] == self.playchar and self.gamematrix[6] == self.playchar:
            return True
        elif self.gamematrix[1] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[7] == "":
            return True
        elif self.gamematrix[1] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[7] == self.playchar:
            return True
        elif self.gamematrix[1] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[7] == self.playchar:
            return True
        elif self.gamematrix[2] == self.playchar and self.gamematrix[5] == self.playchar and self.gamematrix[8] == "":
            return True
        elif self.gamematrix[2] == self.playchar and self.gamematrix[5] == "" and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[2] == "" and self.gamematrix[5] == self.playchar and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[0] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[8] == "":
            return True
        elif self.gamematrix[0] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[0] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[8] == self.playchar:
            return True
        elif self.gamematrix[2] == self.playchar and self.gamematrix[4] == self.playchar and self.gamematrix[6] == "":
            return True
        elif self.gamematrix[2] == self.playchar and self.gamematrix[4] == "" and self.gamematrix[6] == self.playchar:
            return True
        elif self.gamematrix[2] == "" and self.gamematrix[4] == self.playchar and self.gamematrix[6] == self.playchar:
            return True
        else:
            return None

    def secondmove(self):
        if self.compstart[0] == 0 and self.gamematrix[1] == "" and self.gamematrix[2] == "":
            self.gamematrix[1] = self.compchar
            self.compstart[0] = 1
        elif self.compstart[0] == 1 and self.gamematrix[0] == "" and self.gamematrix[2] == "":
            self.gamematrix[0] = self.compchar
            self.compstart[0] = 0
        elif self.compstart[0] == 2 and self.gamematrix[0] == "" and self.gamematrix[1] == "":
            self.gamematrix[0] = self.compchar
            self.compstart[0] = 0
        elif self.compstart[0] == 3 and self.gamematrix[4] == "" and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.compstart[0] == 4 and self.gamematrix[3] == "" and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.compstart[0] == 5 and self.gamematrix[3] == "" and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.compstart[0] == 6 and self.gamematrix[7] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 7 and self.gamematrix[6] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 8 and self.gamematrix[6] == "" and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
            self.compstart[0] = 7
        elif self.compstart[0] == 0 and self.gamematrix[3] == "" and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.compstart[0] == 3 and self.gamematrix[0] == "" and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.compstart[0] == 6 and self.gamematrix[0] == "" and self.gamematrix[3] == "":
            self.gamematrix[3] = self.compchar
            self.compstart[0] = 3
        elif self.compstart[0] == 1 and self.gamematrix[4] == "" and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
            self.compstart[0] = 7
        elif self.compstart[0] == 4 and self.gamematrix[1] == "" and self.gamematrix[7] == "":
            self.gamematrix[7] = self.compchar
            self.compstart[0] = 7
        elif self.compstart[0] == 7 and self.gamematrix[1] == "" and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.compstart[0] == 2 and self.gamematrix[5] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 5 and self.gamematrix[2] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 8 and self.gamematrix[2] == "" and self.gamematrix[5] == "":
            self.gamematrix[5] = self.compchar
            self.compstart[0] = 5
        elif self.compstart[0] == 0 and self.gamematrix[4] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 4 and self.gamematrix[0] == "" and self.gamematrix[8] == "":
            self.gamematrix[8] = self.compchar
            self.compstart[0] = 8
        elif self.compstart[0] == 8 and self.gamematrix[0] == "" and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.compstart[0] == 2 and self.gamematrix[4] == "" and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.compstart[0] == 4 and self.gamematrix[2] == "" and self.gamematrix[6] == "":
            self.gamematrix[6] = self.compchar
            self.compstart[0] = 6
        elif self.compstart[0] == 6 and self.gamematrix[2] == "" and self.gamematrix[4] == "":
            self.gamematrix[4] = self.compchar
            self.compstart[0] = 4
        elif self.emptyspots != []:
            self.gamematrix[random.sample(self.emptyspots, 1)[0]] = self.compchar
        else:
            pass
