from ant import Ant
from control import *
import time


# This is A Program using the Ant Colony Optimization Algorythm to find the minimum value of a multivariable function
# Please read the txt file:'readme.txt' before using it
# Karaiskos Efstathios student at National Technical University of Athens in Civil Engineering (cv22067)
# Course: Computer programming 4o semester
# Feel free to contact with me at: cv22067@mail.ntua.gr or at stathisk2003@gmail.com


# Record the start time of the proces
start_time = time.process_time()

# Initialize the control object
control = Control()

# Calculate initial intervals and starting position
vals = control.calculate_intervals()

# Get the initial best score
best_score = control.score

# Initialize the iteration counter,global pheromone and stored values dictionaries
iteration_count = 0
stored_values ={}
global_pheromone= {}

# Loop until the maximum number of iterations is reached
while iteration_count < control.itt_max:

    # Clear previous iteration score and pheromone dictionary and update iteration counter
    itt_score = None
    itt_pher = {}
    iteration_count += 1

    # Loop through the number of ants
    for n in range(control.ant_count + 1):

        # Create a new ant with current parameters
        ant = Ant(vals, global_pheromone, stored_values, itt_pher)

        # Get the ant's solution that returns its score and deposited pheromones through the path
        score, itt_pher = Ant.move(ant)

        # Update the iteration and best score if a better score was found
        itt_score = control.itter_score(itt_score, score)
        best_score = control.update_score(itt_score, best_score)

    # Update the pheromone and return the stored values and global pheromone dictionaries
    global_pheromone, stored_values = ant.update()
    # Print the current status
    print(f"Iteration number: {iteration_count}  Iteration score: {itt_score[0]:.5f}")
    print(f"Current best score: {best_score[0]:.5f}" + "  At:", [f"{at:.4f}" for at in best_score[1]],'\n')

# Print the final best score and its corresponding parameters
print(f"Final best score: {best_score[0]:.6f}")
print("At:", [f"{at:.4f}" for at in best_score[1]], '\n')

# Calculate and print the elapsed time
elapsed_time = time.process_time() - start_time
print(f"Elapsed time: {elapsed_time} seconds")