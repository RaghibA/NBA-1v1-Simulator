import random
import time
from player import player
    
class Simulation:
    def __init__(self, player1, player2, scoreLimit):
        self.player1 = player1
        self.player2 = player2
        self.scoreLimit = scoreLimit
        self.outcomeQueue = [] # allows us to either iterate over the outcomes of 
                                # each POS, or just jump to the final result

    def __shootForBall(self):
        # players take turn shooting threes to see who gets the first possession
        ballFirst = -1
        shot = False
        ct = 0

        while shot != True:
            # Player 1 shoots for ball - Three point percentage
            if ct == 6: # if it takes more than 6 shots, we can just give player 1 the ball
                self.player1.ball = True
                ballFirst = 1
                break
            if self.player1.ball == False:
                c = random.randrange(101)
                if c < self.player1.tp * 100:
                    self.outcomeQueue.append(self.player1.name + ' made the shot')
                    shot = True
                    self.player1.ball = True
                    ballFirst = 1
                else:
                    self.outcomeQueue.append(self.player1.name + ' shot and missed')
            time.sleep(1)
            # Player 2 shoots for ball - 1 point percentage
            if self.player1.ball == False:
                c = random.randrange(101)
                if c < self.player2.tp * 100:
                    self.outcomeQueue.append(self.player2.name + ' made the shot')
                    shot = True
                    self.player2.ball = True
                    ballFirst = 2
                else:
                    self.outcomeQueue.append(self.player2.name + ' shot and missed')
            
        if ballFirst is 1:
            self.outcomeQueue.append(self.player1.name + ' gets ball first')
            self.player1.ball = True
        else:
            self.outcomeQueue.append(self.player2.name + ' gets ball first')
            self.player2.ball = True

        if self.player1.ball != True:
            self.player1, self.player2 = self.player2, self.player1
        
    def sim(self):
        score = 0
        while score < self.scoreLimit:
            break

    def play(self):
        self.__shootForBall()
