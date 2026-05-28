ANT COLONY OPTIMAZATION ALGORYTHM PROGRAM FOR FINDING MINIMUM VALUE AND LOCATION OF A FUNCTION
CAUTION:THIS IS A EXPERIMENTAL METHOD AND THE IT'S SOLUTION MUST BE EXAMINED BEFORE USE   
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
GENERAL INSTRUCTIONS 
Note 1: For the program to work as intended you can only modify the starting parameters in "__init__" and "f"  methods of "Control" class
Note 2: The "f" method must have the form f(var) where x1,x2,x3,....=var is written in next line of code   
Note 3: x1,x2,x3,.... must be in order of the given limits 
Note 4: Ant count must be an integer and will slow the algorythm a lot if it is a large quantity such as the number of points (N) 
Note 5: We recommend the power of distance (b) to be equal to the pheromone power (a) so the method won't make a fast and inaccurate solution 
Note 5: We recommend a=1 and b=1 (feel free to make tests)
Note 6: Every ant is depositing pheromone in every visited trail. From A to B the deposited pheromone  has a value of Q/(1+abs(f(B))) where Q is selected by the user
Note 7: A trail is being erased from memory if it is smaller than 5% of the max pheromone of all trails
Note 8: To start the program run the script file after choosing all the starting parameters in the "Control" Class(Check Note 1) 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VERSION 1 INSTRUCTIONS
Note 1: This version is inspired by the genetic algoryth method where the fitness function is 1/(1+f(n))
Note 2: The given function must have only positive values 
Note 3: The probability of ant to move from A to B is given by (t^a)*(1/(1+abs(f(B)))^b where t is the pheromone of the path A-B and a and b to constants of the algorythm 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
VERSION 2 INSTRUCTIONS
Note 1: This version is our method of computing the probabiblity of a ant moving from node A to B 
Note 2: The function values is changed by adding numbers so the smaller value is more likely to be selected 
Note 3: Feel free to experiment with this method and tell us your opinion  
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
NATIONAL TECHNICAL UNIVERISTY OF ATHENS , DEPARTMENT OF CIVIL ENGINEERING 
COURSE OF  COMPUTER PROGRAMMING 
STUDENT:EFSTATHIOS KARAISKOS CV22067 4o SEMESTER
EMAIL:cv22067@mail.ntua.gr or at stathisk2003@gmail.com  
 
