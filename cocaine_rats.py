## agent.py
import random

class Action:
    def __init__(self, name, minRW, maxRW):
        self.name = name
        self.minRW = minRW
        self.maxRW = maxRW
        self.truRW = (minRW + maxRW)/2
    
    def do(self):
        return random.randint(self.minRW, self.maxRW)
        
cocaine   = Action("COCAINE", 0, 3)
weed      = Action("WEED", 0, 2)
pellets   = Action("PELLETS", 1, 2)
social    = Action("SOCIAL ", -1, 3)
zapper    = Action("ZAPPER ", -2, -1)
nothing   = Action("NOTHING", 0, 0)

actions = [cocaine,
           weed,
           pellets,
           zapper,
           social,
           nothing]

############
        
class Agent:
    
    def __init__(self, name, tolerance, openness):
        self.name = name
        self.tl = tolerance   ## Tolerate lows better
        self.op = openness    ## Raise predicted reward
        self.xp = {}
        self.scores = []
    
    def do_day(self):
        daily_actions = 4
        actions_pred = {}
        rewards_total = 0
        random.shuffle(actions)
        for action in actions:
            # If action is new, set inherent "curiosity" reward
            if action.name not in self.xp.keys():
                actions_pred[action.name] = self.op
            # Else use average of prior experience
            else:
                prevs = self.xp[action.name]
                actions_pred[action.name] = sum(prevs) / len(prevs)
            # Set predicted value
            print(action.name, " predicted at ", round(actions_pred[action.name], 2))
        
        for i in range (0,daily_actions):
            max_reward_pred_score = 0
            max_reward_pred = nothing
            for action in actions:
                # Find action with best predicted reward
                if actions_pred[action.name] > max_reward_pred_score:
                    max_reward_pred = action
                    max_reward_pred_score = actions_pred[action.name]
            
            # Get reward
            reward = max_reward_pred.do()
            print("DO: ", max_reward_pred.name, " | ", reward)
            # Tolerate negatives
            if reward <= 0:
                reward += self.tl
            # Record rewards permanently
            if max_reward_pred.name not in self.xp.keys():
                self.xp[max_reward_pred.name] = [reward]
            else:
                self.xp[max_reward_pred.name] += [reward]
            
            # Update totals
            rewards_total += reward
        
        # Finish day
        self.scores.append(rewards_total)
        print("Daily mean is ---->        ", (rewards_total/daily_actions))


tolerant_rat_A  = Agent("TolerantRat A ", 1, 2)
open_rat_A      = Agent("OpenRat A     ", 0, 3)
closed_rat_A   = Agent("ClosedRat A    ", 0, 1)
sensitive_rat_A = Agent("SensitiveRat A", -1, 2)

agents = [tolerant_rat_A,
          open_rat_A,
          closed_rat_A,
          sensitive_rat_A]

############

def do_day_all(agents):
    for agent in agents:
        print()
        print("--------> Agent: ", agent.name)
        agent.do_day()

day_limit = 100

print("\nInitiating with agents:")
for agent in agents:
    print("\n| ", agent.name)
    print("--> Tolerance: ", agent.tl)
    print("--> Openness:  ", agent.op)

for i in range(0,day_limit):
    print()
    print("--------> DAY ", i)
    do_day_all(agents)

print()
print("--------> LIFETIME MEAN REWARD")
print()
for agent in agents:
    print(agent.name, " | ", round((sum(agent.scores) / len(agent.scores)), 2))
    print("    Perception error:")
    errs = []
    for action in actions:
        if action.name in agent.xp.keys():
            perceived_util = sum(agent.xp[action.name]) / len(agent.xp[action.name])
            true_util = action.truRW
            err = perceived_util - true_util
            errs += [err]
            print("    > ", action.name, round((err), 2))
        else:
            print("    >  ANA")
    
    sse = 0
    for e in errs:
        sse += e**2
    
    print(">  MSE: ", round((sse / len(errs)), 2))
    print()



    