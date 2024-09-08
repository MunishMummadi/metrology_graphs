import numpy as np
import matplotlib.pyplot as plt

def mandel_statistics_plot():
    # Hypothetical data for interlaboratory measurements
    labs = ['Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5']
    mandel_h = np.random.normal(0, 1, 5)  # Mandel's h statistics (random)
    mandel_k = np.random.normal(1, 0.2, 5)  # Mandel's k statistics (random)

    # Plot Mandel's h
    plt.bar(labs, mandel_h, color='skyblue')
    plt.title("Mandel's h Statistics for Interlaboratory Comparison")
    plt.xlabel("Laboratories")
    plt.ylabel("Mandel's h")
    plt.show()

    # Plot Mandel's k
    plt.bar(labs, mandel_k, color='lightcoral')
    plt.title("Mandel's k Statistics for Interlaboratory Comparison")
    plt.xlabel("Laboratories")
    plt.ylabel("Mandel's k")
    plt.show()

# Call the function
mandel_statistics_plot()
