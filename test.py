from AIMA.probability import *

PW_variables = []
for column in range(1, 4 + 1):
        for row in range(1, 4 + 1):
            PW_variables  = PW_variables  + ['(%d,%d)'%(column,row)]

T, F = True, False
p_true = 0.2
p_false = 1- p_true

var_values = {each: [T, F] for each in PW_variables}
print(var_values)
JPD =JointProbDist(PW_variables,var_values)
events = all_events_jpd(PW_variables, JPD, {})

for each_event in events:
    # Calculate the probability for this event
    # if the value of a variable is false, motiply by p_false which is 0.12, otherwise motiply by p_true which is 1-0.12 
    prob = 1 # initial value of the probability
    for (var, val) in each_event.items(): # for each (variable, value) pair in the dictionary
        prob = prob * p_false if val == F else prob * p_true
    # Assign the probability to this event
    JPD[each_event]= prob
   
for each in PW_variables:
    p = enumerate_joint_ask(each, {}, JPD)
    print(each,  p.show_approx())
