import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation():
    # Set seed for reproducibility
    np.random.seed(123)

    # Simulating input variables
    mean = 5
    std_dev = 1
    x = np.random.normal(mean, std_dev, 1000)
    u = np.random.normal(0, 0.1, 1000)

    # Simulating measurement uncertainty (hypothetical model)
    result = x + u

    # Plotting histogram of the results
    plt.hist(result, bins=30, edgecolor='black', alpha=0.7)
    plt.title("Monte Carlo Simulation of Measurement Uncertainty")
    plt.xlabel("Measured Value")
    plt.ylabel("Frequency")
    plt.show()

# Call the function
monte_carlo_simulation()
