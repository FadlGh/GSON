import json
import matplotlib.pyplot as plt

def visualize_plot(src: str, colors: list, linestyle: str = 'solid', linewidth: int = 1, title: str = 'Graph', x_axis: str = 'x-axis', y_axis: str = 'y-axis', subset_key: str = None):
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

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    plt.title(title)
    plt.show()

def visualize_bar(src: str, colors: list, title: str = 'Bars', x_axis: str = 'x-axis', y_axis: str = 'y-axis', subset_key: str = None):
    with open(src) as f:
        data = json.load(f)
    
    if subset_key:
        if subset_key in data:
            data = data[subset_key]
        else:
            raise KeyError(f"The specified subset key '{subset_key}' does not exist in the JSON data.")
    
    keys = list(data.keys())
    values = list(data.values())

    plt.bar(keys, values, color=colors)

    plt.xlabel(x_axis)
    plt.ylabel(y_axis)

    plt.title(title)
    plt.show()

def visualize_pie(src: str, colors: list, title: str = 'Pie', subset_key: str = None):
    with open(src) as f:
        data = json.load(f)

    if subset_key:
        if subset_key in data:
            data = data[subset_key]
        else:
            raise KeyError(f"The specified subset key '{subset_key}' does not exist in the JSON data.")

    keys = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels = keys, colors=colors,  
        startangle=90, shadow = True, 
        radius = 1.2, autopct = '%1.1f%%') 
  
    plt.legend() 
    plt.title(title)
    plt.show() 

visualize_pie('src/bar.json', colors = ['green', 'yellow', 'red'], subset_key="bar")
