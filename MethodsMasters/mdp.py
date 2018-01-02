import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = GridWorld(path)
        self.directions = self.world.get_directions()
    def create_policy(self):
        #TODO
        directionsTranslator = {0:'u', 1: 'd', 2: 'l', 3: 'r'}
        policy = np.random.randint(0,len(self.directions),self.world.get_size())
        outPol = np.chararray(self.world.get_size())
        for i in range(0,policy.max()+1):
            outPol[policy == i] = directionsTranslator[i]
        outPol[self.world.free_map()] = 'X'
        return outPol.decode('UTF-8')

    def calculate_step(self,x,y,policy):
        gamma = 1
        state = np.array([x,y])
        forward_step = self.world.step(state,policy[x,y])
        if(policy[x,y] == 'u' or policy[x,y] == 'd'):
            side_step_one = self.world.step(state,'l')
            side_step_two = self.world.step(state,'r')
        elif(policy[x,y] == 'l' or policy[x,y] == 'r'):
            side_step_one = self.world.step(state,'u')
            side_step_two = self.world.step(state,'d')
           
        reward = -0.04 +gamma*(0.8* self.world[forward_step]+0.1*self.world[side_step_one]+0.1*self.world[side_step_two])
        return reward
    
    def evaluate_policy(self,policy, max_steps):
        evaluated_policy = np.zeros(shape = policy.shape)
        n = 0
        while(n < max_steps):
            M = self.world.get_size()
            print(M)
            for x in range(M[0]):
                for y in range(M[1]):
                    evaluated_policy[x,y] = mdp.calculate_step(self,x,y,policy) 
            n += 1
        return evaluated_policy
    
    def iterate_policy(self):
        #TODO
        a=5

    def print_solutions(self):
        #TODO
        a=5
        
hallo = mdp('3by4.grid')
testpolicy = hallo.create_policy()
print(hallo.evaluate_policy(testpolicy,1))