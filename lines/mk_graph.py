import matplotlib.pyplot as plt
import pandas as pd

# Output
output_file_name = "figure.pdf"

# The list of `type` in the input csv file
data_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

color_list = [
        '#D13333',
        '#D1AB33',
        '#29A829',
        '#373392',
        '#AAAAAA',
        '#F76709',
        '#F7EF09',
        '#932169',
        ]

# Figure config
plt.figure(figsize=(8, 3))

i = 0
for t in data_list:
    # Plot
    plt.plot([0, len(data_list) + 1], [i + 1, i + 1], markersize=4, marker="*", color=color_list[i])
    plt.plot([i + 1, i + 1], [0, len(data_list) + 1], markersize=4, marker="*", color=color_list[i])

    i = i + 1

# Save to file
plt.savefig(output_file_name, bbox_inches="tight")
