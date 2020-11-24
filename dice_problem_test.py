"""
Which is more likely? 

A) You roll two dice 5 times and, every time, 
one o the two comes up as 1 and the other as 6. 

B) You roll 10 dice all at once. 
5 come up as 1s and the other 5 come up as 6s.

A, B or equal probability?

Below program creates a handful of 2 dice and throws them five times 
and a handful of 10 dice and throws them once. 

Results are converted to a numpy array, sorted and checked against the 'win' array.

Above is repeated by number specified by NUM_TESTS. 



"""
import numpy as np

def check_equal(a,b):
    "Function to check if two arrays are equal"
    if np.array_equal(a,b):
        return 1
    else:
        return 0

class Die:
    """
    Class representing a die

    """

    def __init__(self, colour, sides_count = 6):
        self.__sides_count = sides_count
        self.colour = colour

    def description(self):
        return "A {} die with {} sides".format(self.colour, self.__sides_count)

    def get_sides_count(self):
        """
        Returns the number of sides the die has
        """
        return self.__sides_count

    def roll(self):
        """
        Rolls a die and returns a number from 1
        to the sides count
        """
        import random as _random
        return _random.randint(1, self.__sides_count)

class Handful:
    """
    Class for a handful of dice. 
    """
    def __init__(self,num_dice=1,times_thrown=1):
        self.num_dice = num_dice
        self.times_thrown = times_thrown
    
    def description(self):
        return "A handful of {} die thrown {} times".format(self.num_dice, self.times_thrown)
   
    def throw(self):
        
        colour_list = ['Red', 'Green', 'White', 'Yellow', 'Blue',
                'Black', 'Brown', 'Azure','Ivory', 'Teal']
        die_list = []
        
        for i in colour_list[0:self.num_dice]:
            x = Die(i)
            die_list.append(x)
        
        throw_list = []
        
        for i in range(0,self.times_thrown):
            for x in die_list:
                throw_list.append(x.roll())
                
        throw_array = np.array(throw_list)
        throw_array = np.reshape(throw_array, (self.times_thrown,self.num_dice))
        
        return throw_array

NUM_TESTS = 10
A_win_counter = 0
A_i_list = []

B_win_counter = 0
B_i_list = []

for i in range(1,NUM_TESTS+1):
    a = Handful(2,5)       
    A = (np.sort(a.throw()))
    A_win_array = np.array([[1,6],[1,6],[1,6],[1,6],[1,6]])
    A_win_counter += check_equal(A, A_win_array) #adds 1 to win counter if sorted results match win array
    if check_equal(A, A_win_array) == 1:
        A_i_list.append(i)
        
    print(f'A tests: {i}. A wins: {A_win_counter}')
    
for i in range(1,NUM_TESTS+1):
    b = Handful(10,1)
    B = np.sort(b.throw())
    B_win_array = np.array([[1,1,1,1,1,6,6,6,6,6]])
    B_win_counter += check_equal(B, B_win_array) #adds 1 to win counter if sorted results match win array
    if check_equal(B, B_win_array) == 1:
        B_i_list.append(i)
    print(f'B tests: {i}. B wins: {B_win_counter}')
    
print(f'A wins is equal to {A_win_counter} out of {i})')  
print(f'A win frequency list is: {A_i_list}.')

print(f'B wins is equal to {B_win_counter} out of {i})')
print(f'B win frequency list is: {B_i_list}.')
                                  

