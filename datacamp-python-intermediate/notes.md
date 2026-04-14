# Datacamp - Intermediate Python

**Index**

1. Basic plots with Matplotlib

---

## #1 Basic plots with Matplotlib

Data Visualization

* Very Important in Data Analysis
  * Explore data
  * Report insights

Matplotlib  

There are many visualization packages in Python, but the mother of them all is Matplotlib.


* Matplotlib is essential for creating insightful and visually appealing plots. The subpackage pyplot is commonly imported as plt.

* Line Plots - we can create a line plot to visualize data trends over time.

For example:  

```python
import matplotlib.pyplot as plt
plt.plot(year, pop)
plt.show()
```

This code plots the `year` on the x-axis and `pop` (population) on the y-axis, and displays the plot.

* Scatter Plots - scatter plots are useful for showing the relationship between two variables.

For instance:

```python
plt.scatter(gdp_cap, life_exp)
plt.xscale('log')
plt.show()
```

This code creates a scatter plot with `gdp_cap` on the x-axis and `life_exp` on the y-axis, using a logarithmic scale for the x-axis.

* Interpreting Plots: We can extract meaningful insights from interpreting plots, such as predicting future population growth or understanding the correlation between GDP and life expectancy.

