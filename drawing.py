import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np


class Plotter:
    """Class of draws plots
    """
    def __init__(self):
        """Сreating a target folder"""
        self.plots_dir = 'plots'
        if not os.path.exists(self.plots_dir):
            os.makedirs(self.plots_dir)

    def draw_plots(self, json_file):
        """Drawing plots

        Args:
            json_file (_type_): input data.json

        Returns:
            _type_: list of paths to all plots
        """
        df = pd.read_json(json_file)
        plots_paths = []
        plt.style.use('fivethirtyeight')

        # for 'min', 'mean', 'max' plot
        plt.figure()
        df.boxplot(column=['min', 'mean', 'max'])
        plt.yticks(np.arange(0, df[['min', 'mean', 'max']].max().max() + 10, 10.0))
        plt.title('Boxplot for columns ' + ', '.join(['min', 'mean', 'max']))
        plot_path = os.path.join(self.plots_dir, f'min-mean-max.png')
        #plt.close()
        plt.savefig(plot_path)
        plots_paths.append(plot_path)

        # for another plots

        draw_names = ['min', 'mean', 'max', 'floor', 'ceiling']
        for draw_name in draw_names:
            draw_cols = [col for col in df.columns if draw_name in  col]
            plt.figure()
            df.boxplot(column=draw_cols)
            plt.yticks(np.arange(0, df[draw_cols].max().max() + 10, 10.0))
            plt.title('Boxplot for columns ' + ', '.join(draw_cols))
            plot_path = os.path.join(self.plots_dir, f'{"-".join(draw_cols)}.png')
            #plt.close()
            plt.savefig(plot_path)
            plots_paths.append(plot_path)     

        return plots_paths
