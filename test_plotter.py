import unittest
from drawing import Plotter
import os

class TestPlotter(unittest.TestCase):
    def setUp(self):
        self.plotter = Plotter()
        self.url = 'https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json'

    def test_draw_plots(self):
        plots = self.plotter.draw_plots(self.url)
        self.assertTrue(len(plots) > 0)
        for plot in plots:
            self.assertTrue(os.path.exists(plot))

    def test_plot_file_format(self):
        plots = self.plotter.draw_plots(self.url)
        for plot in plots:
            self.assertTrue(plot.endswith('.png'))

    def test_plot_content(self):
        plots = self.plotter.draw_plots(self.url)
        for plot in plots:
            with open(plot, 'rb') as f:
                content = f.read()
                self.assertTrue(len(content) > 0)

if __name__ == '__main__':
    unittest.main()
