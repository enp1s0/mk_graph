import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

output_file_name = "figure.pdf"

df = pd.read_csv("data.csv", encoding="UTF-8")

array = df.to_numpy().reshape(5, 5)
fig, ax = plt.subplots()
im = ax.imshow(array)
cbar = ax.figure.colorbar(im,
                          ax = ax,
                          shrink=0.5 )

fig.savefig(output_file_name, bbox_inches="tight")
