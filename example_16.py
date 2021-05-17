# NOTE: for naming & design purposes, you may assume the players are directional
#       i.e., `a` is the Player
#             `b` is the Challenger
#       e.g., `rules` could return "player wins" or "player loses"
#              or it could "player wins" vs "challenger wins"
# QUESTION: how do you represent ties?
from random import choice

def rules(a, b):
    ''' return who wins, given shapes played by two players a and b '''
    pass

def random_strategy(history):
    ''' randomly select a shape '''
    return choice(['rps'])

# other sample strategies…

def beat_previous_play(history):
    ''' select the shape that would beat the opponent's previous play '''
    pass

def most_common_play(history):
    ''' select the most common shape from the opponent's previous N plays '''
    pass


games = []
for _ in range(10_000):
    player     = random_strategy(games) 
    challenger = random_strategy(games) 
    games.append((player, challenger))
    

print(games)
results = [rules(a, b) for a, b in games]

# print(results)