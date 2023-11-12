import matplotlib.pyplot as plt 
import json

def visualize_plot(src: str, colors: list, linestyle: str = 'solid', linewidth: int = 1, title: str = 'Graph'):
    with open(src) as f:
        data = json.load(f)

    for i, inner_dict in enumerate(data.values()):
        values_list = list(inner_dict.values())
        x_values = values_list[0]
        y_values = values_list[1]

        if i >= len(colors):
            plt.plot(x_values, y_values, linestyle = linestyle, linewidth = linewidth)
        else:
            plt.plot(x_values, y_values, color = colors[i], linestyle = linestyle, linewidth = linewidth)

    plt.xlabel('x - axis') 
    plt.ylabel('y - axis') 
    
    plt.title(title)
    plt.show()

visualize_plot('src/main.json', colors = ['green'])
