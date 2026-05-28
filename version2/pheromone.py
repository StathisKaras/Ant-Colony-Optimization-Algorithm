class Pheromone():
    def __init__(self, global_pheromone, iteration_pheromone, constants):
        """Initializes the Pheromone object"""
        # Starting pheromone of each trail and evaporation rate
        self.t0=constants[1]
        self.evaporation = constants[0]
        # global pheromone and iteration pheromone dictionaries
        self.global_pheromone=global_pheromone
        self.iteration_pheromone = iteration_pheromone
    def return_pher(self,key):
        """"Checks if the path is already visited and return the corresponding pheromone"""
        # From node A to B the trail pheromone is the same as from node B to A
        rev_key=key[::-1]
        # If the reverse trail has already a value then update this value
        if rev_key in self.global_pheromone:key=rev_key
        # Return the pheromone of the given trail
        return self.global_pheromone.setdefault(key, self.t0)

    def add_pher(self,key,deposit):
        """"Deposits the pheromone that every ant leaves in the path"""
        # Deposits pheromone in  the trail the ant used during each step of the search
        rev_key=key[::-1]
        # If the reverse trail has already a value then update this value
        if rev_key in self.iteration_pheromone:key=rev_key
        self.iteration_pheromone[key] = self.iteration_pheromone.get(key, 0) + deposit
        # Return the iteration pheromone dictionary
        return self.iteration_pheromone

    def update_pher(self):
        """"Updates the global pheromone and deletes low pheromone trails"""
        # Empty list to store all the trails where the pheromone is low in order to delete them from dictionary
        temp=[]
        # Update the global pheromone by evaporation rate and the deposited pheromone in every trail of the iteration
        for key in self.global_pheromone:
            rev_key=key[::-1]
            if rev_key in self.iteration_pheromone:
                self.global_pheromone[key] = (1 - self.evaporation) * self.global_pheromone[key] + self.iteration_pheromone.get(rev_key, 0)
            else:
                self.global_pheromone[key] = (1 - self.evaporation) * self.global_pheromone[key] + self.iteration_pheromone.get(key, 0)
        # Get the max value of the pheromone in the global pheromone dictionary
        max_pheromone = max(self.global_pheromone.values())
        print(f'Current max pheromone: {max_pheromone:.2f}')
        # Cycle the dictionary and delete all the paths with less pheromone than 5% of the max pheromone
        for key in self.global_pheromone:
            if self.global_pheromone[key]<0.05*max_pheromone:temp.append(key)
        for key in temp:del self.global_pheromone[key]
