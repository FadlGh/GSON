# GSON

GSON is a simple python project built to Visualize JSON data as plots, pie and bars.

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

#### **Feel free to contribute to the project**

