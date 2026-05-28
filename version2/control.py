import numpy as np

class Control():
    """Initializes the Control object"""
    def __init__(self,values={}):

        # Only change the values NOT containing 'self.' in their name
        # Also change the f static function below

        # Search space properties

        N=100                                           # number of points per variable
        n=4                                              # number of variables
        limits=([-10,8],[-10,9],[-10,7],[-10,7])         # limits of variables in given order


        #Algorythm properties

        ant_count = int(N / 2)        # number of ants
        itt_max = 30                  # Max iteration number
        Nmax = 8 * n * N /2           # maximum number of steps in a route
        b=1                           # distance power

        #Pheromone properties

        evaporation = 0.05            # pheromone evaporation rate
        t0 = 1                        # pheromone constant in any non visited path
        Q = 0.5                        # pheromone deposit constant
        a = 3                         # pheromone power


        #-----------------------------------------------------------------------------------------------------#
        #-----------------------------------------------------------------------------------------------------#
        #-----------------------------------------------------------------------------------------------------#
        #-----------------------------------------------------------------------------------------------------#
        self.N = N
        self.values=values        # Stored values dictionary
        self.n = n
        self.limits=limits
        self.ant_count =ant_count
        self.itt_max=itt_max
        self.Nmax = Nmax
        self.b = b
        self.evaporation=evaporation
        self.t0=t0
        self.Q=Q
        self.a=a


    @staticmethod
    def f(var):
        """The Function that the method is applied for finding the minimum value """
        x, y, z, w = var
        return -20 * np.exp(-0.2 * np.sqrt(0.25 * (x ** 2 + y ** 2 + z ** 2 + w ** 2))) - np.exp(0.25 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y) + np.cos(2 * np.pi * z) + np.cos(2 * np.pi * w))) + 20 + np.e

    # Minimum value: 0 at (0, 0, 0, 0)
    # Ackley function
    # Domain: x, y, z, w ∈ [-5, 5]



    def calculate_intervals(self):
        """Calculates the parameters of the search space """

        # A list of the distance between 2 points in every dimension
        step = [(self.limits[i][1] - self.limits[i][0]) / self.N for i in range(self.n)]

        # The boundaries of the search space
        starting_points = [self.limits[k][0] for k in range(self.n)]
        endpoints = [self.limits[k][1] for k in range(self.n)]

        # The middle of the search space that every ant starts from
        midpoints = [(self.limits[k][0] + self.limits[k][1]) / 2 for k in range(self.n)]

        # Starting best score
        self.score=Control.f(midpoints),list(midpoints)

        return tuple(step), tuple(starting_points), tuple(endpoints), self.n,tuple(midpoints)
    @staticmethod
    def update_score(it_score, best_score):
        """Updates the score and the position of the minimum"""
        # Return the smallest of the 2 scores with the position that it is located
        if it_score[0]<best_score[0]:return it_score
        else:return best_score
    @staticmethod
    def itter_score(it_score, ant_score):
        """Updates the iteration score and the position of the minimum"""
        # Return the smallest of the 2 scores with the position that it is located
        # If iteration score doesn't  exist return the ant score
        if it_score is None or it_score[0]>ant_score[0]:return ant_score
        else:return it_score