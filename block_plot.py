import numpy as np
import matplotlib.pyplot as plt

def block_plot():
    # Hypothetical block plot data (can represent measurement uncertainty spread)
    labs = ['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']
    block_data = [np.random.normal(100, i, 50) for i in range(1, 6)]

    # Box plot (simulating block plot)
    plt.boxplot(block_data, labels=labs)
    plt.title("Block Plot of Laboratory Measurement Uncertainty")
    plt.xlabel("Laboratories")
    plt.ylabel("Measurement Value")
    plt.show()

# Call the function
block_plot()
