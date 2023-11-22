# GSON

GSON is a simple python project built to Visualize JSON data as plots, pies and bars.

## JSON format to use:

### For Plot:
```json
{
  "p1": {
    "x": [1, 2, 3, 4],
    "y": [2, 4, 3, 4]
  },

  "p2": {
    "x": [1, 2, 3, 4],
    "y": [1, 6, 7, 9]
  },

  "p3": {
    "x": [1, 2, 3, 4],
    "y": [2, 6, 23, 9]
  }

  "..."
}
```
-----

### For Pie & Bars:
```json
{
  "p1": 4,

  "p2": 10,

  "p3": 40,

  "..."
}
```
-----
#### **Note: You can put your data in a sub directory in the JSON file.**
-----

## Functions used in GSON:

### Opening JSON file:
```python
...
    with open(src) as f:
        data = json.load(f)

    if subset_key:
        if subset_key in data:
            data = {subset_key: data[subset_key]}
        else:
            raise KeyError(f"The specified subset key '{subset_key}' does not exist in the JSON data.")
...
```

### Use data for Plot:
```python
...
    for i, inner_dict in enumerate(data.values()):
        values_list = list(inner_dict.values())
        x_values = values_list[0]
        y_values = values_list[1]
...
```

### Use data for Pie & Bars:
```python
...
    keys = list(data.keys())
    values = list(data.values())
...
```
-----
## Call Functions

### For Plot:
```python
visualize_plot(src: str, colors: list, linestyle: str = 'solid', linewidth: int = 1, title: str = 'Graph', x_axis: str = 'x-axis', y_axis: str = 'y-axis', subset_key: str = None)
```
### For Pie:
```python
visualize_pie(src: str, colors: list, title: str = 'Pie', subset_key: str = None)
```
### For Bars:
```python
visualize_bar(src: str, colors: list, title: str = 'Bars', x_axis: str = 'x-axis', y_axis: str = 'y-axis', subset_key: str = None)
```

## Images:
![2](https://github.com/FadlGh/GSON/assets/97055147/f1b33b40-0dfe-41b8-880b-81d9a67ea5fc)
![3](https://github.com/FadlGh/GSON/assets/97055147/5b997909-af1a-4ca4-8f7d-2fb8cdf8c1cc)
![1](https://github.com/FadlGh/GSON/assets/97055147/afe74193-241b-43b1-af17-6a2f420217d8)


#### **Feel free to contribute to the project**

