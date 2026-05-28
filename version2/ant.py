from random import randint,random
from control import Control
from pheromone import Pheromone
class Ant():
    """Initializes the Ant object"""
    def __init__(self,vals,global_pheromone,stored_values,itteration_pheromone):
        """Initializes the Ant class with parameters."""
        # Search space properties
        self.step,self.spoint,self.endpoint,self.n,self.midpoint= vals
        # Each ant starts in the middle of the search space
        self.position=list(self.midpoint)
        self.at=list(self.position)
        self.current_value=Control.f(self.position)
        self.score=Control.f(self.position)
        # Initialize control and Pheromone classes
        self.control=Control(stored_values)
        self.it_pher = itteration_pheromone
        self.pheromone=Pheromone(global_pheromone,itteration_pheromone,(self.control.evaporation,self.control.t0))
        # A dictionary of all the positions an ant will visit is each route
        self.visited={}


    def check(self,f1,f2):
        """Checks if values have different signs and makes changes to them."""
        # Checks if any node is already visited and returns 0 fot the heuristic value of the node
        if None in (f1,f2):return Ant.checkNone(f1,f2)
        if 0 in (f1,f2):return Ant.checkzero(f1,f2)

        if f1*f2>0:
            if f1>0:return f1,f2
            else:return f1+max(abs(f1),abs(f2))+1,f2+max(abs(f1),abs(f2))+1

        else:
            if f1>0:return f1+abs(f2)+1,1
            else:return 1,f2+abs(f1)+1


    @staticmethod
    def checkNone(f1,f2):
        """Handles cases where one or both differences are None."""
        if f1 is None and f2 is not None :
            if f2!=0:
                return (0, abs(f2))
            else: return (0,1)
        elif f2 is None and f1 is not None:
            if f1!=0:
                return (abs(f1),0)
            else:return(1,0)
        else: return 1,1
    @staticmethod
    def checkzero(f1,f2):
        """Handles cases where one or both differences are 0."""
        if f1==0:
            if f2<0 and f2!=-1:return abs(f2)+1,1
            elif f2>0:return 1,f2+1
            else:return 1,1
        else:
            if f1>0 :return f1+1,1
            elif f1<0 and f1!=-1:return 1,abs(f1)+1
            else:return 1,1


    def already_calculated(self,position):
        """Checks if the position is already calculated."""
        # If the position is already calculated it searches in the stored values dictionary and returns  the fitness value
        # Else the position is added to the dictionary and the fitness value is returned
        return self.control.values.setdefault(tuple(position),Control.f(tuple(position)))


    def computevalues(self):
        """Computes the values of a selected variable and checks if they have been already computed"""
        # Select a random number that represents in which variable the ant will move at
        self.rand = randint(0, self.n - 1)
        # Step of randomly selected variable
        self.selected_step = self.step[self.rand]
        # Empty lists that correspond to the value and pheromone that goes to the heuristic function and the fitness function value
        fit_vals=[]
        pher = []
        heu_vals=[]
        # Create a copy of the  ant's position and find the probability to move to the 2 nearest node of the selected variable
        for i in (1,-1):
            temporary_position = list(self.position)
            temporary_position[self.rand] = self.position[self.rand] + i * self.selected_step
            # Get the value of the fitness function in the 2 positions
            fitness_value = self.already_calculated(temporary_position)
            fit_vals.append(fitness_value)
            # Checks if the position is already visited in this route
            if tuple(temporary_position) in self.visited:
                heu_vals.append(None)
                pher.append(0.01)
            # If the position hasn't been visited in this route
            else:
                heu_vals.append(fitness_value)
                pher.append(self.pheromone.return_pher((tuple(self.position),tuple(temporary_position))))
        # Make all the changes to the heuristic values so the smaller value is more likely to be selected
        (val1,val2)=self.check(heu_vals[0],heu_vals[1])
        # Keep track of the fitness values of the 2 nodes
        self.value1=fit_vals[0]  # + selected step node
        self.value2=fit_vals[1]  # - selected step node
        return (val1,val2),pher


    def chance(self):
        """Returns the probability tuple."""
        # Initialize 2 empty list one temporary and one for the probability
        P=[]
        temp=[]
        # Ask for the value and pheromone of each node
        (value,pher)=self.computevalues()
        # Calculate the probability tuple
        for v,p in zip(value,pher):
            if v==0:
                temp.append(0)
                continue
            temp.append((v**self.control.b)*(p**self.control.a))
        for i in temp:
            P.append(i/sum(temp))
        return tuple(P)

    def choice(self):
        """Returns a random choice of movement in the selected variable."""
        # Ask for the probability tuple
        P = self.chance()
        # Make the choice list
        I = [sum(P[:i+1]) for i in range(2)]
        # Select a random number between 0  and 1
        rand_val = random()
        # If the number is smaller than the choice list's number the corresponding choice is selected
        for ch in range(2):
            if rand_val <= I[ch]:
                # Return 0 if choice is + selected step and if choice is - selected step
                return ch

    def ant_score_check(self):
        """Checks and updates the ant's score."""
        # If the ant finds a better score the score and it's position is updated
        if self.score>self.current_value:self.score,self.at=(self.current_value, self.position[:])

    def move(self):
        """Moves the ant through the solution space."""
        # Initialize the step counter
        step_count=0
        # Loop until the max step number is exceeded or if a search space boundary has been reached
        while step_count<self.control.Nmax:
            ch=self.choice()
            # Save the current position
            previous_position=list(self.position)
            # Change the current position and value and checks the score
            if ch==0:
                self.position[self.rand]+= self.selected_step
                # Add the new node to the ant visited dictionary
                self.visited[tuple(self.position)]=True
                self.current_value=self.value1
                self.ant_score_check()
            else:
                self.position[self.rand] -= self.selected_step
                self.visited[tuple(self.position)] = True
                self.current_value=self.value2
                self.ant_score_check()
            # Add pheromone to the path (previous position,current position)
            self.it_pher = self.pheromone.add_pher((tuple(previous_position),tuple(self.position)), abs(self.control.Q /(1+abs(self.current_value))))
            # If a search space boundary has been reached break the loop
            if self.position[self.rand] == self.endpoint[self.rand] or self.position[self.rand] == self.spoint[self.rand]:break
            # Update the step counter
            step_count += 1
        # Return the score and it's position and the updated iteration pheromone dictionary
        return (self.score,self.at),self.it_pher
    def update(self):
        """Updates the pheromone trail."""
        # Update pheromone
        self.pheromone.update_pher()
        # Return the global pheromone and the stored values dictionaries
        return self.pheromone.global_pheromone,self.control.values