import matplotlib.pyplot as plt
import pandas as pd

# Output
output_file_name = "figure.pdf"

# The list of `type` in the input csv file
type_list = ['A', 'B']

# Figure config
plt.figure(figsize=(8, 3))
plt.xlabel("X")
plt.ylabel("Y")
#plt.yscale("log", base=10)
plt.grid()

# Load input data
df = pd.read_csv("data.csv", encoding="UTF-8")

for t in type_list:
    # Filter the input data
    df_t = df.query("type=='" + t + "'")

    # Plot
    plt.plot(df_t['x'], df_t['y'], label="Type" + t, markersize=4, marker="*")

#plt.annotate('', (1, 10), (1, 20), arrowprops=dict(facecolor='darkgray', shrink=0., width=2, headwidth=6))
#plt.text(1.1, 15, 'better', ha="center", va="center", rotation=90)

# Legend config
plt.legend(loc='best',
       ncol=len(type_list))

# Save to file
plt.savefig(output_file_name, bbox_inches="tight")
