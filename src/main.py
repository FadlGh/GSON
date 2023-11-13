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

def visualize_bar(src: str, colors: list, tick_labels: str = None, title: str = 'Bars', subset_key: str = None):
    with open(src) as f:
        data = json.load(f)
    
    if subset_key:
        if subset_key in data:
            data = {subset_key: data[subset_key]}
        else:
            raise KeyError(f"The specified subset key '{subset_key}' does not exist in the JSON data.")
    
    left = []
    for i in range(len(data)):
        left.append(i)


    values = list(data.values())
    height_values = []

    for j in range(len(values)):
        height_values.append(values[j])

    print(height_values)
    
    if tick_labels:
        tick_labels = tick_labels[:len(values)]
        plt.bar(left, height_values, color = colors, tick_labels = tick_labels)
    else:
        plt.bar(left, values, color = colors)

    plt.xlabel('x - axis')
    plt.ylabel('y - axis')

    plt.title(title)
    plt.show()


visualize_bar('src/bar.json', colors = ['green'])
