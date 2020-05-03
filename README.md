# bbplot
> Extending the base style plots in Python.


This project try to reproduce the visualization in the [BBC R cookbook] an(https://bbc.github.io/rcookbook/)  with Python. You can use the theme come with it to make your chart looks nicer.



`pip install bbplot`

## How to use
Pick one library that you like.
1. altair (if you have never use R before, I recommend altair as it can create interactive chart easily)
2. plotnine (similar to ggplot2 in R)

## plotnine

## altair

```python
import altair as alt
from bbplot.custom_theme import bbc_theme
alt.themes.register("custom", bbc_theme)
alt.themes.enable("custom")
```




    ThemeRegistry.enable('custom')



Add this 3 extra lines in your plot, it will style your charts automatically.
