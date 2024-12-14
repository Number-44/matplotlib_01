import matplotlib.pyplot as plt
import numpy as np

# Setting the figure size
plt.figure(figsize=(8, 6))

# Title and labels
plt.title("This is the Title: OMG", fontsize=20)
plt.xlabel("X Axis", fontsize=10)
plt.ylabel("Y Axis", fontsize=10)

# Grid and axis limits
plt.grid(True)
plt.xlim(0, 20)
plt.ylim(0, 20)

# Ticks
plt.xticks(np.arange(0, 21, 5), fontsize=8)  # Adjust tick range and font size
plt.yticks(fontsize=8)

# Scatter plot, text, and lines
x = np.arange(0, 20)
y = np.arange(0, 20)
plt.scatter(x, y, c="orange", label="Points")
plt.text(x=15, y=3, s="Like a mark!", fontsize=10, color="purple")
plt.vlines(x=0, ymin=0, ymax=20, colors="green", label="Vertical Line")
plt.hlines(y=0, xmin=0, xmax=20, colors="blue", label="Horizontal Line")

# Adding a legend
plt.legend()

# Show the plot
plt.show()

# Final print statement
print("Hello, Matplotlib!")
