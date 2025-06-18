# quickplots

A small Python package providing quick, ready-to-use plot classes wrapping pandas, matplotlib, and seaborn. Simply import the class you need and call `.plot(...)` on your DataFrame or Series, then `.show()` to render.

## Quickstart

```python
from quickplots import LinePlot, HeatmapPlot
import pandas as pd

# load your data
df = pd.read_csv('data.csv')

# make a line plot
LinePlot().plot(df, x='date', y='value', title='My Trend').show()

# make a heatmap
pivot = df.pivot('category', 'month', 'value')
HeatmapPlot().plot(pivot, annot=True, cmap='viridis', title='Monthly Heatmap').show()
```

---