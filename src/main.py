import json
import matplotlib.pyplot as plt

def visualize_plot(src: str, colors: list, linestyle: str = 'solid', linewidth: int = 1, title: str = 'Graph', subset_key: str = None):
    with open(src) as f:
        data = json.load(f)

    if subset_key:
        if subset_key in data:
            data = {subset_key: data[subset_key]}
        else:
            raise KeyError(f"The specified subset key '{subset_key}' does not exist in the JSON data.")

    for i, inner_dict in enumerate(data.values()):
        values_list = list(inner_dict.values())
        x_values = values_list[0]
        y_values = values_list[1]

        if i >= len(colors):
            plt.plot(x_values, y_values, linestyle=linestyle, linewidth=linewidth)
        else:
            plt.plot(x_values, y_values, color=colors[i], linestyle=linestyle, linewidth=linewidth)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title(title)
    plt.show()

def visualize_bar(src):
    with open(src) as f:
        data = json.load(f)

visualize_plot('src/main.json', colors = ['green'])
