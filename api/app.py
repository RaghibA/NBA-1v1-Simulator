from sim import Simulation
from player import player

#    def __init__(self, name, fieldGoalPercentage, threePointPercentage, 
#         fieldGoalsTaken, threePointsAttemps, rebounds, blocks, steals):
def __main__():
    lbj = player('Lebron', .5, .34, 19.6, 4.4, 7.4, .8, 1.6)
    kobe = player('Kobe', .447, .329, 19.5, 4.1, 5.2, .5, 1.4)

    sim = Simulation(lbj,kobe,21)
    sim.play()

if __name__ == '__main__':
    __main__()