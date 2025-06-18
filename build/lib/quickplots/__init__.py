# This file defines what symbols are exposed when you do `from quickplots import ...`.
# It pulls your plot classes from `plots.py` so users can access them directly.
# The `from .plots import ...` syntax is a relative import: it looks for `plots.py` in the same folder (the `quickplots/` directory).
# That `plots.py` file lives alongside this `__init__.py` inside the `quickplots` package.
__version__ = "0.1.0"
from .plots import (
    LinePlot,
    BarPlot,
    ScatterPlot,
    HistogramPlot,
    BoxPlot,
    HeatmapPlot,
)