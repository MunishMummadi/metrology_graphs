#### **Overview**
This repository contains Python scripts that generate visualizations related to **statistical metrology**. These scripts simulate measurement uncertainty and analyze interlaboratory comparison data. While the original statistical functions are available in R via the **metRology** package, this project uses Python to generate similar visualizations, focusing on measurement uncertainty, Monte Carlo simulations, and statistical methods for interlaboratory studies.

#### **Scripts Included**
1. **Monte Carlo Simulation of Measurement Uncertainty**  
   Simulates measurement uncertainty using the Monte Carlo method and outputs a histogram representing the distribution of measurement results. This visualization helps to understand the variation and uncertainty in measurement results.
   - **Script**: `monte_carlo_simulation.py`
   - **Plot**: Histogram of measurement uncertainty.
2. **Mandel's h and k Statistics Visualization**  
   Generates plots for **Mandel's h** and **Mandel's k** statistics, which are widely used in interlaboratory comparisons to detect outliers and assess consistency across laboratories.
   - **Script**: `mandel_h_k_visualization.py`
   - **Plots**: Separate plots for Mandel's h and Mandel's k statistics.
3. **Key Comparison Plot**  
   This script visualizes the results of interlaboratory comparisons through a **Key Comparison Plot**, displaying how laboratory results compare with reference values, with uncertainty bars representing variability.
   - **Script**: `key_comparison_plot.py`
   - **Plot**: Key comparison plot showing laboratory results and uncertainties.
4. **Block Plot for Laboratory Measurement Uncertainty**  
   Generates a block plot to visualize measurement uncertainty across different laboratories in an interlaboratory comparison, providing an overview of variability and consistency.
   - **Script**: `block_plot.py`
   - **Plot**: Block plot for visualizing grouped laboratory uncertainties.
#### **Dependencies**
All visualizations are created using Python libraries, especially **Matplotlib** for plotting. Ensure the following Python libraries are installed:
- `matplotlib` (for plotting)
- `numpy` (for numerical simulations)
Install these dependencies using the following command:
```bash
pip install matplotlib numpy
```
#### **How to Run the Scripts**
1. Clone the repository:
   ```bash
   git clone https://github.com/MunishMummadi/metrology_graphs
   cd metrology_graphs
   ```
2. Run any of the provided Python scripts to generate the respective visualization. For example, to run the Monte Carlo simulation:
   ```bash
   python monte_carlo_simulation.py
   ```
Each script will generate and display the corresponding plot, which can be saved and used in presentations or reports.
