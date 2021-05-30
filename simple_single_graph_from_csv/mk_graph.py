import matplotlib.pyplot as plt
import pandas as pd

# Output format
output_file_extension = "png"

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

# Legend config
plt.legend(loc='best',
       bbox_to_anchor=(0, 1.3, 1., -.1),
       borderaxespad=0.,
       ncol=len(type_list),
       mode="expand")

# Save to file
plt.savefig("result." + output_file_extension, bbox_inches="tight")
