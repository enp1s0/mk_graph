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

# Load input data
df = pd.read_csv("data.csv", encoding="UTF-8")

# Create graph
fig, axs = plt.subplots(fig_block_m, fig_block_n, figsize=(10, 6))

line_list = []
label_list = []
for i in range(fig_block_n):
    for j in range(fig_block_m):
        v = i + j * 3 + 1
        # Plot
        for t in type_list:
            axs[j][i].set_title('x' + str(v))
            #axs[j][i].set_xscale('log', base=2)
            l = axs[j][i].plot(
                    df['x'],
                    df[t] * v,
                    markersize=4,
                    marker="*",
                    color=color_table[t])
            if i == 0 and j == 0:
                line_list += [l]
                label_list += [t]

                #axs[j][i].annotate('', (0, 7), (0, 8), arrowprops=dict(facecolor='darkgray', shrink=0., width=2, headwidth=6))
                #axs[j][i].text(0.2, 7.5, 'better', ha="center", va="center", rotation=90)

# Legend config
fig.legend(line_list,
           labels=label_list,
           loc='upper center',
           ncol=len(type_list),
           bbox_to_anchor=(0.5, 1.0)
           )

# Save to file
#fig.subplots_adjust(hspace=0)
fig.savefig(output_file_name, bbox_inches="tight")
