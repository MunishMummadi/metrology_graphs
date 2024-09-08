import numpy as np
import matplotlib.pyplot as plt

def key_comparison_plot():
    # Hypothetical lab results data
    labs = ['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']
    lab_means = np.random.normal(100, 5, 5)  # Lab means
    lab_uncertainty = np.random.uniform(1, 3, 5)  # Lab uncertainties

    # Dot and error bars plot
    plt.errorbar(labs, lab_means, yerr=lab_uncertainty, fmt='o', capsize=5, color='green')
    plt.title("Key Comparison Plot for Interlaboratory Studies")
    plt.xlabel("Laboratories")
    plt.ylabel("Measurement Result")
    plt.grid(True)
    plt.show()

# Call the function
key_comparison_plot()
