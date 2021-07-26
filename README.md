# cocaine rat simulator 2021

# cocainerats
Small behavioural psych simulator featuring customisable rats and actions.

Each day the rats pick a task to perform based on max predicted utility and their "openness to experience" trait.
Actual utility received is recorded as experience, attenuated by "pain tolerance", and used to pick tasks in later days. 

Tasks generate utility randomly between a set min and max. Tasks and utility values are as follows:

- Nothing ( 0,  0)
- Pellets ( 1,  2)
- Cocaine ( 0,  3)
- Social  (-1,  2)
- Zapper  (-2, -1)

More tasks are easily added.

The default rats are:

OpenRat
 - Tolerance 0
 - Openness  3

ClosedRat
- Tolerance 0
- Openness  1

TolerantRat
 - Tolerance 1
 - Openness  2

SensitiveRat
 - Tolerance -1
 - Openness 2
  
By default the rats perform 4 tasks a day over a 5 day session.
At the end of each session the rats' "perception error" for each action, and total MSE, is recorded. 
Positive error reflects a bias towards that action. 

Possible expansions:

- Use of varied functions to randomise utility output for certain activities, i.e. logistic curve
- Lifetime loss function such as hunger or boredom to discourage certain activities and encourage others
