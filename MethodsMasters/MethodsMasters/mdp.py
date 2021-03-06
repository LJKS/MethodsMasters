import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = GridWorld(path)

    def create_policy(self):
        #TODO
        directions = GridWorld.getSize(self.world)
        print(directions)


    def evaluate_policy(self,policy, max_steps):
        evaluated_policy = np.zeros(shape = policy.shape)
        while(n < max_steps):
            for x,y in range(self.world):
                evaluated_policy[x,y] = calculate_step(x,y,policy) 
            n += 1
        return evaluated_policy
    
    def calculate_step(self,x,y,policy):
        gamma = 1
        state = np.array([x,y])
        forward_step = GridWorld.step(state,policy[x,y])
        if(policy[x,y] == 'u' or policy[x,y] == 'd'):
            side_step_one = GridWorld.step(state,'l')
            side_step_two = GridWorld.step(state,'r')
        elif(policy[x,y] == 'l' or policy[x,y] == 'r'):
            side_step_one = GridWorld.step(state,'u')
            side_step_two = GridWorld.step(state,'d')
           
        reward = -0.04 +gamma*(0.8* self.world[forward_step]+0.1*self.world[side_step_one]+0.1*self.world[side_step_two])
        return reward
    
    def iterate_policy(self):
        #TODO
        a=5

    def print_solutions(self):
        #TODO
        a=5
        
hallo = mdp('3by4.grid')
hallo.create_policy()
