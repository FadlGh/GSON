import unittest
from src import main

class TestVisualizations(unittest.TestCase):

    def test_visualize_plot(self):
        result = main.visualize_plot('tests/graph.json', colors=['blue', 'orange'])
        self.assertIsNone(result) 

    def test_visualize_bar(self):
        result = main.visualize_bar('tests/bar-pie.json', colors=['green', 'yellow', 'red'])
        self.assertIsNone(result)

    def test_visualize_pie(self):
        result = main.visualize_pie('tests/bar-pie.json', colors=['purple', 'cyan', 'pink'])
        self.assertIsNone(result) 

if __name__ == '__main__':
    unittest.main()
