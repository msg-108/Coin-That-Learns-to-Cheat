#import libraries
import random
import matplotlib.pyplot as plt

# Parameters 
while True:
    try:
        total_tosses = int(input("Total number of tosses: "))
        if total_tosses <= 0:
            raise ValueError
        break
    except ValueError:
        print("Total tosses must be a positive integer")

while True:
    try:
        true_bias = float(input("True bias (0-1): "))
        if true_bias < 0 or true_bias > 1:
            raise ValueError
        break
    except ValueError:
        print("Bias must be a number between 0 and 1")

alpha = 50   # prior heads (Beta parameter)
beta = 50   # prior tails (Beta parameter)

prob_history = []

#Simulation loop
for i in range(total_tosses):
    random_number = random.random() # Generates a random float between 0.0 and 1.0

    if random_number <= true_bias:
        outcome = 1 # heads
    else:
        outcome = 0 # tails

    # Bayesian update
    if outcome == 1:
        alpha += 1
    else:
        beta += 1

    # Posterior mean estimate
    prob_history.append(alpha / (alpha+ beta))

# Plotting
plt.plot(prob_history, label="Bayesian Estimate P(Heads)")
plt.axhline(true_bias, linestyle="--", label="True Bias")
plt.xlabel("Toss number")
plt.ylabel("Estimated probability of heads")
plt.title("Bayesian Learning of Coin Bias (Beta–Bernoulli)")
plt.legend()
plt.show()