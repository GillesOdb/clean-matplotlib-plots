# About
This repository contains Python scripts for creating clean visuals with Matplotlib.

Inspired by <a href="https://www.principiae.be/">Jean-luc Doumont</a>.

# Example plots

## General
- Notice how you don't need to rotate your head to read the y axis label
- Easily add graph letters a), b), c), ... 
<img src="https://github.com/GillesOdb/clean-matplotlib-plots/blob/main/default_plot/output_plot.png" width="400">

## Error bar - different colors
- Enter x data as a list
- Enter y data as a list of lists
- The number of values in x_data should be equal to the number of lists in y_data
- The number of values in the y_data sublists is not important

```
x_data = [10,20,30,40]
y_data = [[1,2,3,4,5],[2,5,6,7,8,31,7],[1,2,54,53,3,2,5,1,0],[1,2,5,66,7,4,2]]
```

<img src="https://github.com/GillesOdb/clean-matplotlib-plots/blob/main/errorbar_plot_different_colors/output_plot.png" width="400">


- Optionally add jitter

<img src="https://github.com/GillesOdb/clean-matplotlib-plots/blob/main/errorbar_plot_different_colors/output_plot_with_jitter.png" width="400">

## Horizontal bar plot
- Enter data as dict
- Automagically sorted from high to low

```
# Your data
items = [
    {'name': "Liam", 'age': 55},
    {'name': "Olivia", 'age': 35},
    {'name': "Noah", 'age': 45},
    {'name': "Emma", 'age': 28},
    {'name': "Oliver", 'age': 19},
    {'name': "Isabella", 'age': 60},
]
```

<img src="https://github.com/GillesOdb/clean-matplotlib-plots/blob/main/horizontal_barplot/horizontal_barplot.png" width="400">
 
## Intensity plot - 2D heatmap
- Enter data as 2D array
```
# Example 16 x 16 array
input_list =   [[10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,20,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,25,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,30,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,35,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,40,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,45,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,50,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,55,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,60,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,55,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,50,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,45,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35],]
```
<img src="https://github.com/GillesOdb/clean-matplotlib-plots/blob/main/intensity_plot/output_plot.png" width="600">
