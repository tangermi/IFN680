
#----- IFN680 Assignment 1 -----------------------------------------------#
#  The Wumpus World: a probability based agent
#
#  Implementation of two functions
#   1. PitWumpus_probability_distribution()
#   2. next_room_prob()
#
#    Student no: PUT YOUR STUDENT NUMBER HERE
#    Student name: PUT YOUR NAME HERE
#
#-------------------------------------------------------------------------#
from random import *
from AIMA.logic import *
from AIMA.utils import *
from AIMA.probability import *
from tkinter import messagebox
from logic_based_move import next_room

#--------------------------------------------------------------------------------------------------------------
#
#  The following two functions are to be developed by you. They are functions in class Robot. If you need,
#  you can add more functions in this file. In this case, you need to link these functions at the beginning
#  of class Robot in the main program file the_wumpus_world.py.
#
#--------------------------------------------------------------------------------------------------------------
#   Function 1. PitWumpus_probability_distribution(self, width, height)
#
# For this assignment, we treat a pit and the wumpus equally. Each room has two states: 'empty' or 'containing a pit or the wumpus'.
# A Boolean variable to represent each room: 'True' means the room contains a pit/wumpus, 'False' means the room is empty.
#
# For a cave with n columns and m rows, there are totally n*m rooms, i.e., we have n*m Boolean variables to represent the rooms.
# A configuration of pits/wumpus in the cave is an event of these variables.
#
# The function PitWumpus_probability_distribution() below is to construct the joint probability distribution of all possible
# pits/wumpus configurations in a given cave, two parameters
#
# width : the number of columns in the cave
# height: the number of rows in the cave
#
# In this function, you need to create an object of JointProbDist to store the joint probability distribution and  
# return the object. The object will be used by your function next_room_prob() to calculate the required probabilities.
#
# This function will be called in the constructor of class Robot in the main program the_wumpus_world.py to construct the
# joint probability distribution object. Your function next_room_prob() will need to use the joint probability distribution
# to calculate the required conditional probabilities.
#
def PitWumpus_probability_distribution(self, width, height): 
    # Create a list of variable names to represent the rooms. 
    # A string '(i,j)' is used as a variable name to represent a room at (i, j)
    self.PW_variables = [] 
    for column in range(1, width + 1):
        for row in range(1, height + 1):
            self.PW_variables  = self.PW_variables  + ['(%d,%d)'%(column,row)]

    #--------- Add your code here -------------------------------------------------------------------
    T, F = True, False
    p_true = 0.2
    p_false = 1 - p_true

    var_values = {each: [T, F] for each in self.PW_variables}
    print(var_values)
    JPD =JointProbDist(self.PW_variables,var_values)
    events = all_events_jpd(self.PW_variables, JPD, {})

    for each_event in events:
        # Calculate the probability for this event
        # if the value of a variable is false, motiply by p_false which is 0.12, otherwise motiply by p_true which is 1-0.12 
        prob = 1 # initial value of the probability
        for (var, val) in each_event.items(): # for each (variable, value) pair in the dictionary
            prob = prob * p_false if val == F else prob * p_true
        # Assign the probability to this event
        JPD[each_event]= prob
    
    #for each in self.PW_variables:
        #p = enumerate_joint_ask(each, {}, JPD)
        #print(each,  p.show_approx())

    return JPD
                
        
#---------------------------------------------------------------------------------------------------
#   Function 2. next_room_prob(self, x, y)
#
#  The parameters, (x, y), are the robot's current position in the cave environment.
#  x: column
#  y: row
#
#  This function returns a room location (column,row) for the robot to go.
#  There are three cases:
#
#    1. Firstly, you can call the function next_room() of the logic-based agent to find a
#       safe room. If there is a safe room, return the location (column,row) of the safe room.
#    2. If there is no safe room, this function needs to choose a room whose probability of containing
#       a pit/wumpus is lower than the pre-specified probability threshold, then return the location of
#       that room.
#    3. If the probabilities of all the surrounding rooms are not lower than the pre-specified probability
#       threshold, return (0,0).
#
def next_room_prob(self, x, y):
    #messagebox.showinfo("Not yet complete", "You need to complete the function next_room_prob.")
    pass
    #--------- Add your code here -------------------------------------------------------------------
    logic_based_check = next_room(self,x,y)
    if  logic_based_check != (0,0):
        return logic_based_check
    else:
        #get query rooms
        surrounding = self.getsurronding(x,y)
        for each in self.visited_rooms:
            if each in surrounding:
                query = surrounding.remove(each)
        
        #get unknowns
        all_rooms = []
        for column in range(1, 5):
            for row in range(1, 5):
                all_rooms.append((column,row))
        for each in self.visited_rooms:
            all_rooms.remove(each)
        for each in query:
            all_rooms.remove(each)
        unknowns = all_rooms

        #get BS_known
        BS_known = self.observation_breeze_stench(self,self.visited_rooms)




        #calculate 𝛼

        #get events
        #events = all_events_jpd(self.PW_variables, self.jdP_PWs, {})

        #calculate 𝜬(𝐵𝑆_𝑘𝑛𝑜𝑤𝑛 |𝑃𝑞,𝑃𝑊_𝑘𝑛𝑜𝑤𝑛,𝑦)
        P_sum = 0
        evidence = self.observation_pits(self,self.visited_rooms)
        for each in unknowns:
            events = all_events_jpd(self.PW_variables,self.jdP_PWs, evidence)
            for each_event in events:
                P_sum += self.consistent(self,BS_known,each_event)
        
        #calculate P
        p = P_sum * 0.2
        print(p)



        return (0,0)

    

            



#---------------------------------------------------------------------------------------------------
 
####################################################################################################
