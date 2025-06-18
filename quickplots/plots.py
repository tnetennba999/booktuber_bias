# This is where all your plotting logic lives. Each class (e.g., `LinePlot`, `HeatmapPlot`) wraps seaborn/matplotlib code.
# You import these classes in your scripts, call their `.plot(...)` methods with your DataFrame or Series,
# and then invoke `.show()` to display the figure.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class BasePlot:
    """Base class for common setup and style."""
    def __init__(self, style: str = "darkgrid", figsize: tuple = (10, 6)):
        sns.set_style(style)
        self.fig, self.ax = plt.subplots(figsize=figsize)

    def show(self):
        plt.show()

class LinePlot(BasePlot):
    """Simple line chart wrapper."""
    def plot(self, data: pd.DataFrame, x: str, y: str, **kwargs):
        title = kwargs.pop('title', f"Line: {y} vs {x}")
        sns.lineplot(data=data, x=x, y=y, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self

class BarPlot(BasePlot):
    """Simple bar chart wrapper."""
    def plot(self, data: pd.DataFrame, x: str, y: str, **kwargs):
        title = kwargs.pop('title', f"Bar: {y} by {x}")
        sns.barplot(data=data, x=x, y=y, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self

class ScatterPlot(BasePlot):
    """Simple scatter chart wrapper."""
    def plot(self, data: pd.DataFrame, x: str, y: str, **kwargs):
        title = kwargs.pop('title', f"Scatter: {y} vs {x}")
        sns.scatterplot(data=data, x=x, y=y, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self

class HistogramPlot(BasePlot):
    """Histogram wrapper."""
    def plot(self, data: pd.Series, bins: int = 10, **kwargs):
        title = kwargs.pop('title', "Histogram")
        sns.histplot(data=data, bins=bins, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self

class BoxPlot(BasePlot):
    """Boxplot wrapper."""
    def plot(self, data: pd.DataFrame, x: str = None, y: str = None, **kwargs):
        title = kwargs.pop('title', f"BoxPlot: {y or 'values'} by {x or 'index'}")
        sns.boxplot(data=data, x=x, y=y, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self

class HeatmapPlot(BasePlot):
    """Heatmap wrapper with customizable colormap and annotations."""
    def plot(self, data: pd.DataFrame, annot: bool = False, fmt: str = ".2f", cmap: str = 'viridis', **kwargs):
        title = kwargs.pop('title', "Heatmap")
        sns.heatmap(data, annot=annot, fmt=fmt, cmap=cmap, ax=self.ax, **kwargs)
        self.ax.set_title(title, fontsize=14)
        return self
