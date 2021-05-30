import matplotlib.pyplot as plt
import pandas as pd

output_file_extension = "pdf"

type_list = ['A', 'B']

plt.figure(figsize=(8, 3))
plt.xlabel("X")
plt.ylabel("Y")
#plt.yscale("log", base=10)
plt.grid()

df = pd.read_csv("data.csv", encoding="UTF-8")

for t in type_list:
    df_t = df.query("type=='" + t + "'")
    plt.plot(df_t['x'], df_t['y'], label="Type" + t, markersize=4, marker="*")

plt.legend(loc='best',
       bbox_to_anchor=(0, 1.3, 1., -.1),
       borderaxespad=0.,
       ncol=len(type_list),
       mode="expand")
plt.savefig("result." + output_file_extension, bbox_inches="tight")
