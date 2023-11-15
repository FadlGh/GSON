import json
import matplotlib.pyplot as plt
from src import main

# Test for visualize_plot
def test_visualize_plot():
    main.visualize_plot('tests/graph.json', colors=['blue', 'orange'])

# Test for visualize_bar
def test_visualize_bar():
    main.visualize_bar('tests/bar-pie.json', colors=['green', 'yellow', 'red'])

# Test for visualize_pie
def test_visualize_pie():
    main.visualize_pie('tests/bar-pie.json', colors=['purple', 'cyan', 'pink'])

if __name__ == "__main__":
    test_visualize_plot()
    test_visualize_bar()
    test_visualize_pie()