"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from maze_env import Maze
from RL_brain import QLearningTable
import pandas as pd

def update1():
    reward_avg = 0
    for cycle in range(10):
        LoopCount = 100
        rewardtable = pd.Series([0]*LoopCount)
        reward_value = 0
        
    
        for episode in range(LoopCount):
              # initial observation
          observation = env.reset()
                 
          while True:
              # refresh env
              env.render()
    
              # RL choose action based on observation
              action = RL.choose_action(str(observation))
    
              # RL take action and get next observation and reward
              observation_, reward, done = env.step(action)
    
              # RL learn from this transition
              RL.learn(str(observation), action, reward, str(observation_))
    
              # swap observation
              observation = observation_
    
                  # break while loop when end of this episode
              if done:
                  reward_value += reward
                  rewardtable[episode] = reward_value
                  break
              
        rewardtable.plot()
        print('Result:',reward_value)
        reward_avg += reward_value
        reward_value = 0
        rewardtable.loc[:] = 0
        RL.q_table.loc[:,:] = 0
    


    reward_avg /= 10
    print('Result_avg:',reward_avg)
    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    env.after(50, update1)
    env.mainloop()