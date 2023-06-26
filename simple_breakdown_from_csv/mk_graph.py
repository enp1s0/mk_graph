import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def draw_breakdown(ax):
    ax.grid(True, axis='y')
    ax.set_title('breakdown', fontsize=global_fontsize)
    ax.set_ylabel('[%]')

    x_list = ['XXX', 'YYY', 'ZZZ']
    label_table = {
            'A' : 'AAA',
            'B' : 'BBB',
            'C' : 'CCC',
            }

    bar_list = []
    label_list = []

    df = pd.read_csv("data.csv", encoding="UTF-8")
    print(df)
    df = df.drop(columns=['X'])

    x_position_list = []
    for j, x in enumerate(x_list):

        tag = f"s_{x}"
        df_t = df[df['name'] == tag]
        df_t = df_t.drop(columns=['name'])
        total = 0
        for y in df_t:
            total += df_t[y].to_numpy()[0]
        for y in df_t:
            df_t[y] /= total / 100
        order = ['B', 'C', 'A']
        df_t = df_t[order]
        print(df_t)

        n_rows, n_cols = df_t.shape
        positions = j * 2
        x_position_list += [positions]
        hatch_list = ['//', '++', '.', '||', '**', 'o', 'xx', '\\\\']
        colors = plt.get_cmap("tab20c")(np.linspace(0.1, 0.6, n_cols))
        edgecolor = '#333333'

        offsets = np.zeros(n_rows, dtype=df_t.values.dtype)
        for i in range(len(df_t.columns)):
            print(df_t.iloc[:, i])
            bar = ax.bar(positions + 0, df_t.iloc[:, i], bottom=offsets, color=colors[i], edgecolor=edgecolor, linewidth=1, hatch=hatch_list[i])
            offsets += df_t.iloc[:, i]

            if j == 0:
                bar_list += [bar]
                label_list += [label_table[df_t.columns[i]]]

    ax.legend(bar_list, label_list, loc='lower right', fontsize=10)
    ax.set_xlabel('name')
    ax.set_xticks(x_position_list, x_list)

# Output
output_file_name = "figure.pdf"
fig_block_m = 1
fig_block_n = 1

# Create graph
fig, axs = plt.subplots(fig_block_m, fig_block_n, figsize=(6, 3.1))

draw_breakdown(axs)

# Save to file
fig.tight_layout()
fig.subplots_adjust(hspace=0)
fig.savefig(output_file_name, bbox_inches="tight")
