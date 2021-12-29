import matplotlib.pyplot as plt
import pandas as pd

# Output
output_file_name = "figure.pdf"
fig_block_m = 2
fig_block_n = 3

# The list of `type` in the input csv file
type_list = ['A', 'B', 'C', 'D', 'E', 'F']
color_table = {
        'A' : 'red',
        'B' : 'blue',
        'C' : 'yellow',
        'D' : 'orange',
        'E' : 'green',
        'F' : 'purple',
        }

# Figure config
plt.figure(figsize=(8, 3))
plt.xlabel("X")
plt.ylabel("Y")
#plt.yscale("log", base=10)
plt.grid()

# Load input data
df = pd.read_csv("data.csv", encoding="UTF-8")

# Create graph
fig, axs = plt.subplots(fig_block_m, fig_block_n, figsize=(10, 6))

type_index = 0
line_list = []
label_list = []
for i in range(fig_block_n):
    for j in range(fig_block_m):
        v = i + j * 3 + 1
        # Plot
        for t in type_list:
            axs[j][i].set_title('x' + str(v))
            l = axs[j][i].plot(
                    df['x'],
                    df[t] * v,
                    markersize=4,
                    marker="*",
                    color=color_table[t])
            if v == len(type_list):
                line_list += [l]
                label_list += [t]

        # inc type_index
        type_index += 1

# Legend config
fig.legend(line_list,
        labels=label_list,
        loc='upper center',
        ncol=len(type_list))

# Save to file
fig.savefig(output_file_name, bbox_inches="tight")
