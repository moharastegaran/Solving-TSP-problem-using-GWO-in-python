import CostFunction_GWO as fit
import random
import numpy
import matplotlib.pyplot as plt

Max_iter = 30
lb = -10
ub = 10
dim = 30
SearchAgents_no = 5

# initialize alpha, beta, and delta_pos
# there are only three leader wolves in the group, as alpha, beta and delta
# as we initialize vector for each leader wolf, we set its indexes to
# infinite, so we can update later.

Alpha_pos = numpy.zeros(dim)
Alpha_score = float("inf")

Beta_pos = numpy.zeros(dim)
Beta_score = float("inf")

Delta_pos = numpy.zeros(dim)
Delta_score = float("inf")

# we may have only one pair of boundary for every dim or sepearte boundaries
# for each dim, so for the ease of use, we cast numeric bounaries to 1d array 
if not isinstance(lb, list):
    lb = [lb] * dim
    print(lb)
if not isinstance(ub, list):
    ub = [ub] * dim

# Initialize the positions of search agents
# We set random values as score for each and every pair (wolf, dim)
# Then we take into accounts these values and update them with their
# more accurate values
Positions = numpy.zeros((SearchAgents_no, dim))
for i in range(dim):
    Positions[:, i] = numpy.random.uniform(0, 1, SearchAgents_no) * (ub[i] - lb[i]) + lb[i]

# We initialize this convergence array to capture alpha_score at each iteration
Convergence_curve = numpy.zeros(Max_iter)

# Main loop, stop condition : maximum iteration reached
for l in range(0, Max_iter):
    for i in range(0, SearchAgents_no):

        # Return back the search agents that go beyond the boundaries of the search space
        # if the score is betwewen lb & up, don't change its value
        for j in range(dim):
            Positions[i, j] = numpy.clip(Positions[i, j], lb[j], ub[j])

            # Calculate cost function for each search agent
            fitness = fit.fitness_1(Positions[i, :])

            # Update Alpha, Beta, and Delta
            if fitness < Alpha_score:
                Alpha_score = fitness;  # Update alpha
                Alpha_pos = Positions[i, :].copy()

            if (fitness > Alpha_score and fitness < Beta_score):
                Beta_score = fitness  # Update beta
                Beta_pos = Positions[i, :].copy()

            if (fitness > Alpha_score and fitness > Beta_score and fitness < Delta_score):
                Delta_score = fitness  # Update delta
                Delta_pos = Positions[i, :].copy()

        # a decreases linearly from 2 to 0
        a = 2 - l * ((2) / Max_iter)

        # In the previous loop, we updated alpha, beta and delta wolves,
        # Now we update omega search agents coordination according to them
        for i in range(0, SearchAgents_no):
            for j in range(0, dim):
                r1 = random.random()  # r1 is a random number in [0,1]
                r2 = random.random()  # r2 is a random number in [0,1]

                A1 = 2 * a * r1 - a  # Equation (3.3)
                C1 = 2 * r2  # Equation (3.4)

                D_alpha = abs(C1 * Alpha_pos[j] - Positions[i, j])  # Equation (3.5)-part 1
                X1 = Alpha_pos[j] - A1 * D_alpha  # Equation (3.6)-part 1

                r1 = random.random()
                r2 = random.random()

                A2 = 2 * a * r1 - a  # Equation (3.3)
                C2 = 2 * r2  # Equation (3.4)

                D_beta = abs(C2 * Beta_pos[j] - Positions[i, j])  # Equation (3.5)-part 2
                X2 = Beta_pos[j] - A2 * D_beta  # Equation (3.6)-part 2

                r1 = random.random()
                r2 = random.random()

                A3 = 2 * a * r1 - a  # Equation (3.3)
                C3 = 2 * r2  # Equation (3.4)

                D_delta = abs(C3 * Delta_pos[j] - Positions[i, j])  # Equation (3.5)-part 3
                X3 = Delta_pos[j] - A3 * D_delta  # Equation (3.5)-part 3

                Positions[i, j] = (X1 + X2 + X3) / 3  # Equation (3.7)

            # we store alpha_score at the end of every iteration to plot cost of
            # current iteration
            Convergence_curve[l] = Alpha_score

            # we print the best fitness at each iteration
            print(['At iteration ' + str(l) + ' the best fitness is ' + str(Alpha_score)])

# Data for plotting, as iteration number for xAxis and best cost function as yAxis
plt.plot(Convergence_curve)
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost Function in Iterations')
plt.show()
