import numpy as np
import matplotlib.pyplot as plt

def compare_uncertainty_methods():
    # Generate traditional GUM and Monte Carlo uncertainty estimates (random example data)
    gum_values = np.random.normal(5, 0.1, 1000)
    mc_values = np.random.normal(5, 0.2, 1000)

    # Scatter plot
    plt.scatter(gum_values, mc_values, alpha=0.5)
    plt.title("Comparison Between GUM-based and Monte Carlo Simulation")
    plt.xlabel("GUM-Based Uncertainty")
    plt.ylabel("Monte Carlo Uncertainty")
    plt.grid(True)
    plt.show()

# Call the function
compare_uncertainty_methods()
