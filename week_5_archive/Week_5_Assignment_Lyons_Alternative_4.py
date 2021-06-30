#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:02:34 2021

@author: earle

Title: Week 5 Assignment Lyons
Date: 11JUN2021
Author: Earle Lyons
Purpose: Create three Matplotlib visuals for Week 5 Assignment
    - Combined Plot = Line Plot & Vertical Bar Plots
    - Discrete Distribution Horizontal Bar Plot
    - Vertical 100% Stacked Bar Plot
    - Vertical Stacked Bar Plot
    - Vertical Bar Plot
    
Inputs: 
Outputs: 
Notes:
     MSDS670 Data Visualization (Regis University)
     21M8W1: 05/03/21-06/27/21
     
Data Source: https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/
"""

# Import libraries
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dpi = 300

# Reset Matplotlib rcParams to default
# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults
mpl.rc_file_defaults()

# Customize Matplotlib with black for text, axes, xtick, and ytick
# Resources:
# https://stackoverflow.com/questions/48958208/how-do-you-change-the-default-font-color-for-all-text-in-matplotlib
# https://matplotlib.org/stable/tutorials/introductory/customizing.html
# https://github.com/empathy87/storytelling-with-data
#mpl.rcParams['text.color'] = '#76787B'
#mpl.rcParams['axes.labelcolor'] = '#76787B'
#mpl.rcParams['xtick.color'] = '#76787B'
#mpl.rcParams['ytick.color'] = '#76787B'
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc_sgskip.html
# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#default-values-and-styling
# https://github.com/edwardtufte/et-book
# plt.rcParams['font.family'] = 'serif'
# plt.rcParams['font.serif'] = ['ETBembo']

# Create the pandas DataFrames for the first Matplotlib visual
# Read 'Overall Homeless' sheet from the
# '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx" Excel workbook into
# 'df1' pandas DataFrame object
# Set index to 'State'
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
df1 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless', index_col='State')

# The 'Total' column is saved to 's_totals' pandas Series object
# The index from the 's_totals' pandas Series object is saved to 'years' list object
# The values from the 's_totals' pandas Series object is saved to 'totals' list object
s_totals = df1.loc['Total']
years = s_totals.index.tolist()
totals = s_totals.values.tolist()

# Read 'Overall Homeless %' sheet from the
# '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx" Excel workbook into
# 'df2' pandas DataFrame object
# Set index to 'State'
df2 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless %', index_col='State')

# The 'Total' column is multiplied by 100 and rounded to two decimals and
# saved to 's_percent_totals' pandas Series object
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.multiply.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html
s_percent_totals = df2.loc['Total'].multiply(100).round(2)
# https://stackoverflow.com/questions/45989858/format-decimals-as-percentages-in-a-column
s_percent_totals_labels = s_percent_totals.astype(str) + '%'

# The index from the 's_percent_totals' pandas Series object is saved to 'percent_years' list object
# The values from the 's_percent_totals' pandas Series object is saved to 'percent_totals' list object
# The values from the 's_percent_totals_labels' pandas Series object is saved to 'percent_totals_labels' list object
percent_years = s_percent_totals.index.tolist()
percent_totals = s_percent_totals.values.tolist()
percent_totals_labels = s_percent_totals_labels.values.tolist()

# Create the first Matplotlib visual
# https://stackoverflow.com/questions/54473465/aligning-x-axis-with-sharex-using-subplots-and-colorbar-with-matplotlib
# https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8,6), constrained_layout=True)
# ax1 plot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
ax1.set_title('U.S. Overall Homeless 2007-2020', loc='left')
# Make all spines invisible
# https://matplotlib.org/stable/gallery/ticks_and_spines/spines_dropped.html
ax1.spines.right.set_visible(False)
ax1.spines.left.set_visible(False)
ax1.spines.top.set_visible(False)
ax1.spines.bottom.set_visible(False)
ax1.plot(years, totals, color='#174A7E')
# ax1 points, text, and annotations
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
ax1.scatter(2007, 641665, s=20, color='#174A7E')
ax1.text(2006, 636000, '2007', color='#174A7E')
ax1.text(2006, 630000, '641,665', color='#174A7E')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html
# https://stackoverflow.com/questions/44489900/arrow-properties-in-matplotlib-annotate
# https://stackoverflow.com/questions/47074423/how-to-get-default-blue-colour-of-matplotlib-pyplot-scatter/47074742
ax1.scatter(2010, 630836, s=60, c='#C3514E')
ax1.annotate('In 2010, there was a 0.99% increase; reaching 630,836',
             xy=(2010, 630836),
             xytext=(2011, 640000),
             arrowprops=dict(arrowstyle='->', color='#C3514E',
                            connectionstyle='arc3, rad=0.15'),
             color='#C3514E')
ax1.scatter(2016, 544084, s=60, color='#C3514E')
ax1.scatter(2020, 575714, s=60, color='#C3514E')
ax1.text(2012.5, 612000, 'Between 2016 and 2020, there were consistent increases', 
         color='#C3514E')
ax1.annotate('',
             xy=(2016, 544084),
             xytext=(2014, 610000),
             arrowprops=dict(arrowstyle='->', color='#C3514E',
                            connectionstyle='arc3, rad=0.15'))
ax1.annotate('',
             xy=(2020, 575714),
             xytext=(2014, 610000),
             arrowprops=dict(arrowstyle='->', color='#C3514E',
                            connectionstyle='arc3, rad=0.15'))
ax1.scatter(2016, 544084, s=20, color='#174A7E')
ax1.scatter(2020, 575714, s=20, color='#174A7E')
ax1.text(2016, 556000, '2016', color='#174A7E')
ax1.text(2016, 550000, '544,084', color='#174A7E')
ax1.text(2020, 586000, '2020', color='#174A7E')
ax1.text(2020, 580000, '575,714', color='#174A7E')
# ax1 ticks
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html
ax1.xaxis.set_tick_params(which='both', labelbottom=False, colors='white')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html
ax1.set_xticks([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html
ax1.set_xticklabels([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
ax1.set_yticks([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html
ax1.set_yticklabels([])
# ax2 plot
# A for loop collects colors in the 'col' list object based on the value
# https://stackoverflow.com/questions/33476401/color-matplotlib-bar-chart-based-on-value
col = []
for val in s_percent_totals:
    if val < 0:
        col.append('#174A7E')
    else:
        col.append('#C3514E')
# Make all spines invisible
# https://matplotlib.org/stable/gallery/ticks_and_spines/spines_dropped.html
ax2.spines.right.set_visible(False)
ax2.spines.left.set_visible(False)
ax2.spines.top.set_visible(False)
ax2.spines.bottom.set_visible(False)
plot = ax2.bar(percent_years, s_percent_totals, color=col)
ax2.set_xlabel('Years')
# ax2 ticks
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.tick_params.html
ax2.xaxis.set_tick_params(which='both')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html
ax1.set_xticks(percent_years)
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticklabels.html
ax1.set_xticklabels(percent_years)
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylim.html
ax2.set_ylim(bottom=-8, top=8)
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
ax2.set_yticks([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html
ax2.set_yticklabels([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html
ax2.bar_label(plot, labels=percent_totals_labels, padding=3)
plt.show()
plot1_filename = 'week_5_matplotlib_lyons_1_11JUN21_old.png'
fig.savefig(plot1_filename, dpi=dpi)

# Create the pandas DataFrames for the second Matplotlib visual
# Read 'Overall Homeless Age Categories' sheet from the
# '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx" Excel workbook into
# 'df3' pandas DataFrame object
df3 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless Age Categories')

# The columns from the 'df3' pandas DataFrame are saved to the 'category_names' list object
# The 'category_names' list is sliced from 1 to 4 and saved to the 'category_names' list object
category_names = df3.columns.tolist()
category_names = category_names[1:4]

# The 'df3' pandas DataFrame is used to create the 'results' dict object with the 'Years' column as the index 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
# https://stackoverflow.com/questions/26716616/convert-a-pandas-dataframe-to-a-dictionary
results = df3.set_index('Years').T.to_dict('list')

# Create the second Matplotlib visual
# References: 
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/horizontal_barchart_distribution.htm
# https://towardsdatascience.com/stacked-bar-charts-with-pythons-matplotlib-f4020e4eb4a7
labels = list(results.keys())
data = np.array(list(results.values()))
data_cum = data.cumsum(axis=1)
category_colors = ['#174A7E', '#BFBEBE', '#C3514E']
fig, ax = plt.subplots(figsize=(8, 6))
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
ax.set_title('U.S. Overall Homeless By Age Group 2013-2020', loc='left')
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())
# Make all spines invisible
# https://matplotlib.org/stable/gallery/ticks_and_spines/spines_dropped.html
ax.spines.right.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax.barh(labels, widths, left=starts, height=0.65,
                    label=colname, color=color)   
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html
    ax.bar_label(rects, label_type='center', color='black')
# The legend is plotted with the length of category_names columns in the upper 
# left of the plot with small fontsize and no frame
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
ax.legend(ncol=len(category_names), bbox_to_anchor=(0,1.015),
          loc='upper left', fontsize='small', frameon=False)
plt.show()
plot2_filename = 'week_5_matplotlib_lyons_2_11JUN21_old.png'
fig.savefig(plot2_filename, dpi=dpi)

# Create the second Matplotlib visual (second alternative)
# References:
# https://pythonmatplotlibtips.blogspot.com/2018/11/normalized-stacked-barplot-number-percentage-python-matplotlib.html
# Create the 'years', 'age_under_18', 'age_18_to_24', and 'age_above_24' list objects
years = df3['Years'].iloc[::-1].tolist()
age_under_18 = df3['< 18'].iloc[::-1].tolist()
age_18_to_24 = df3['18 - 24'].iloc[::-1].tolist()
age_above_24 = df3['> 24'].iloc[::-1].tolist()
# Format values to use commas to separate thousands
# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
age_under_18_fmt = []
for val in age_under_18:
    age_under_18_fmt.append(f'{val:,}')

age_18_to_24_fmt = []    
for val in age_18_to_24:
    age_18_to_24_fmt.append(f'{val:,}')

age_above_24_fmt = []    
for val in age_above_24:
    age_above_24_fmt.append(f'{val:,}')
# Create numpy arrays from 'age_under_18', 'age_18_to_24', and 'age_above_24' list objects
age_under_18_array = np.array(age_under_18)
age_18_to_24_array = np.array(age_18_to_24)
age_above_24_array = np.array(age_above_24)
# Set width of the bars
width = 0.50
age_under_18_array = np.array(age_under_18)
age_18_to_24_array = np.array(age_18_to_24)
age_above_24_array = np.array(age_above_24)
width = 0.50  # the width of the bars
fig, ax = plt.subplots(figsize=(10,5))
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
ax.set_title('U.S. Overall Homeless By Age Group 2013-2020', loc='left')
# Create vertical stack bars
rect1 = ax.bar(years, age_under_18_array, width, color='#174A7E', label='Under 18')
rect2 = ax.bar(years, age_18_to_24_array, width, color='#BFBEBE', bottom=age_under_18_array, label='18 to 24')
rect3 = ax.bar(years, age_above_24_array, width, color='#C3514E', bottom=age_under_18_array+age_18_to_24_array, label='Over 24')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
ax.set_yticks([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html
ax.set_yticklabels([])
# https://matplotlib.org/stable/gallery/ticks_and_spines/spines_dropped.html
ax.spines.right.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)
# The legend is plotted with the length of category_names columns in the upper 
# left of the plot with small fontsize and no frame
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
ax.legend(ncol=len(category_names), bbox_to_anchor=(0,1.015),
          loc='upper left', fontsize='small', frameon=False)
# Add text annotation of the values for each age category
# A for loop iterates through the values in val, xpos, ypos, and yval in the
# zip object to establish labels and positions
# The labels are plotted to the positions with ax.text
# https://pythonmatplotlibtips.blogspot.com/2018/11/sample-number-stacked-barplot-python-matplotlib.html
for val, xpos, ypos, yval in zip(age_under_18_fmt, years, age_under_18_array/2, age_under_18_array):
    ax.text(xpos, ypos, val, color='white', ha="center", va="center")
for val, xpos, ypos, yval in zip(age_18_to_24_fmt, years, age_under_18_array+age_18_to_24_array/2, age_18_to_24_array):
    ax.text(xpos, ypos, val, color='black', ha="center", va="center")
for val, xpos, ypos, yval in zip(age_above_24_fmt, years, age_18_to_24_array+age_18_to_24_array+age_above_24_array/2, age_above_24_array):
    ax.text(xpos, ypos, val, color='black', ha="center", va="center")
fig.tight_layout()
plt.show()
plot2b_filename = 'week_5_matplotlib_lyons_2b_11JUN21_old.png'
fig.savefig(plot2b_filename, dpi=dpi)

# Create the pandas DataFrames for the third Matplotlib visual
# Read 'Overall Over 24' sheet from the
# '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx" Excel workbook into
# 'df4' pandas DataFrame object
df4 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Over 24')

# The 'Years' column from the 'df4' pandas DataFrame are saved to the 'over24_years' list object
# The 'Sheltered Individuals' column from the 'df4' pandas DataFrame are saved to the 'sheltered_individuals' list object
# The 'Unsheltered Individuals' column from the 'df4' pandas DataFrame are saved to the 'unsheltered_individuals' list object
# The 'Sheltered People in Families' column from the 'df4' pandas DataFrame are saved to the 'sheltered_families' list object
# The 'Unsheltered People in Families' column from the 'df4' pandas DataFrame are saved to the 'unsheltered_families' list object
over24_years = df4['Years'].tolist()
sheltered_individuals = df4['Sheltered Individuals'].tolist()
unsheltered_individuals = df4['Unsheltered Individuals'].tolist()
sheltered_families = df4['Sheltered People in Families'].tolist()
unsheltered_families = df4['Unsheltered People in Families'].tolist()

# Create the third Matplotlib visual
# References: 
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
# https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
x = np.arange(len(over24_years))  # the label locations
width = 0.20  # the width of the bars
fig, ax = plt.subplots(figsize=(10,5))
rects1 = ax.bar(x + 0.0, sheltered_individuals, width, color='#E6BAB7', label='Sheltered Individuals')
rects2 = ax.bar(x + 0.2, unsheltered_individuals, width, color='#C3514E', label='Unsheltered Individuals')
rects3 = ax.bar(x + 0.4, sheltered_families, width, color='#BFBEBE', label='Sheltered Families')
rects4 = ax.bar(x + 0.6, unsheltered_families, width, color='#A6A6A5', label='Unsheltered Families')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_title('U.S. Overall Homeless Over Age 24 2016-2020', loc='left')
ax.set_xticks(x + 0.3)
ax.set_xticklabels(over24_years)
ax.set_ylabel('People')
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticks.html
ax.set_yticks([])
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_yticklabels.html
ax.set_yticklabels([])

# Make all spines invisible
# https://matplotlib.org/stable/gallery/ticks_and_spines/spines_dropped.html
ax.spines.right.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)

# Create a for loop that goes through the properties of rects2 object
# The for loop gets the height, width, x, and y from the rects2 object
# The rects2_height has the values for the rects2 object and is format values 
# to use commas to separate thousands
# The rects2 object x and width are used to position the label on the x-axis
# The rects2 object y and height are used to position the label on the y-axis
# The labels are plotted with ax.text
# https://stackoverflow.com/questions/41296313/stacked-bar-chart-with-centered-labels
for rect in rects2:
    rects2_height = rect.get_height()
    rects2_width = rect.get_width()
    rects2_x = rect.get_x()
    rects2_y = rect.get_y()
    # https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
    rects2_label_text = f'{rects2_height:,}'
    # ax.text(x, y, text)
    rects2_label_x = rects2_x + rects2_width/2
    rects2_label_y = rects2_y + rects2_height + 1000
    ax.text(rects2_label_x, rects2_label_y, rects2_label_text, ha='center')

# The legend is plotted with four columns in the upper left of the plot with
# small fontsize and no frame
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
ax.legend(ncol=4, bbox_to_anchor=(0,1.015),
          loc='upper left', fontsize='small', frameon=False)

fig.tight_layout()
plt.show()
plot3_filename = 'week_5_matplotlib_lyons_3_11JUN21_old.png'
fig.savefig(plot3_filename, dpi=dpi)