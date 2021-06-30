#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 19:02:34 2021

@author: earle

Title: Week 5 & 6 Assignment Lyons
Date: 13JUN2021
Author: Earle Lyons
Purpose: Create three Matplotlib visuals for Week 5 Assignment
    - Combined Plot = Line Plot & Vertical Bar Plots
    - Slopegraph Plot
    - Vertical Bar Plot
    
Inputs: 
Outputs: 
Notes:
     MSDS670 Data Visualization (Regis University)
     21M8W1: 05/03/21-06/27/21
     
Data Source: https://www.hudexchange.info/resource/3031/pit-and-hic-data-since-2007/
Data File: '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx"
"""

 #%% Import libraries

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Set DPI
dpi = 300

 #%% Reset Matplotlib rcParams to default

# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rc_file_defaults
mpl.rc_file_defaults()

 #%% Create DataFrames for first Matplotlib visual

# Read 'Overall Homeless' sheet from the Excel workbook and create
# 'df1' pandas DataFrame object and set index to 'State'
df1 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless', index_col='State')

# Index and values are derived the 'Total' column
s_totals = df1.loc['Total']
years = s_totals.index.tolist()
totals = s_totals.values.tolist()

# Read 'Overall Homeless %' sheet from the Excel workbook and create
# 'df2' pandas DataFrame object and set index to 'State'
df2 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless %', index_col='State')

# Create percentages from 'Total' column
s_percent_totals = df2.loc['Total'].multiply(100).round(2)
s_percent_totals_labels = s_percent_totals.astype(str) + '%'

# Index and values are derived the calculated percentages
percent_years = s_percent_totals.index.tolist()
percent_totals = s_percent_totals.values.tolist()
percent_totals_labels = s_percent_totals_labels.values.tolist()

 #%% Create the first Matplotlib visual
 
# https://stackoverflow.com/questions/54473465/aligning-x-axis-with-sharex-using-subplots-and-colorbar-with-matplotlib
# https://matplotlib.org/stable/tutorials/intermediate/constrainedlayout_guide.html
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8,6), constrained_layout=True)
# Create ax1 plot
ax1.set_title('U.S. Overall Homeless 2007-2020', loc='left')
ax1.spines.right.set_visible(False)
ax1.spines.left.set_visible(False)
ax1.spines.top.set_visible(False)
ax1.spines.bottom.set_visible(False)
ax1.plot(years, totals, color='#174A7E')
ax1.scatter(2007, 641665, s=20, color='#174A7E')
ax1.text(2006, 636000, '2007', color='#174A7E')
ax1.text(2006, 630000, '641,665', color='#174A7E')
# https://stackoverflow.com/questions/44489900/arrow-properties-in-matplotlib-annotate
# https://stackoverflow.com/questions/47074423/how-to-get-default-blue-colour-of-matplotlib-pyplot-scatter/47074742
ax1.scatter(2010, 630836, s=60, c='#C3514E')
ax1.annotate('In 2010, there was a 0.99% increase; reaching 630,836',
             xy=(2010, 630836),
             xytext=(2011, 640000),
             arrowprops=dict(arrowstyle='->', color='#C3514E',
                            connectionstyle='arc3, rad=0.15'),
             color='#C3514E')
ax1.annotate('New York experienced the greatest increase; increasing 4,539 from 2009',
             xy=(2010, 630836),
             xytext=(2011, 634000),
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
# Set ax1 labels and ticks
ax1.xaxis.set_tick_params(which='both', labelbottom=False, colors='white')
ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.set_ylabel('People', color='#174A7E')
ax1.set_yticks([])
ax1.set_yticklabels([])

# Create ax2 plot
# https://stackoverflow.com/questions/33476401/color-matplotlib-bar-chart-based-on-value
col = []
for val in s_percent_totals:
    if val < 0:
        col.append('#174A7E')
    else:
        col.append('#C3514E')
plot = ax2.bar(percent_years, s_percent_totals, color=col)
# Make all spines invisible
ax2.spines.right.set_visible(False)
ax2.spines.left.set_visible(False)
ax2.spines.top.set_visible(False)
ax2.spines.bottom.set_visible(False)
# Set ax1 labels and ticks
ax2.set_xlabel('Years')
ax2.xaxis.set_tick_params(which='both')
ax2.set_xticks(percent_years)
ax2.set_xticklabels(percent_years)
ax2.set_ylabel('Change', color='black')
ax2.set_ylim(bottom=-8, top=8)
ax2.set_yticks([])
ax2.set_yticklabels([])
ax2.bar_label(plot, labels=percent_totals_labels, padding=3)
# Display and save the plot
plt.show()
plot1_filename = 'week_5_matplotlib_lyons_1_13JUN21.png'
fig.savefig(plot1_filename, dpi=dpi)

 #%% Create DataFrame for second Matplotlib visual
 
# Read 'Overall Homeless Age Categories sheet from the Excel workbook and create
# 'df3' pandas DataFrame object
df3 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Homeless Age Categories')

# Create lists
years = df3['Years'].iloc[::-1].tolist()
years_slope = [years[0], years[-1]]
age_under_18 = df3['< 18'].iloc[::-1].tolist()
age_under_18_slope = [age_under_18[0], age_under_18[-1]]
age_18_to_24 = df3['18 - 24'].iloc[::-1].tolist()
age_18_to_24_slope = [age_18_to_24[0], age_18_to_24[-1]]
age_above_24 = df3['> 24'].iloc[::-1].tolist()
age_above_24_slope = [age_above_24[0], age_above_24[-1]]

 #%% Create the second Matplotlib visual

# References:
# https://pythonmatplotlibtips.blogspot.com/2018/11/normalized-stacked-barplot-number-percentage-python-matplotlib.html
# Create ax plot
fig, ax = plt.subplots(figsize=(6,6))
ax.plot(years_slope, age_under_18_slope, color='#174A7E', label='Under 18', linewidth=3.0)
ax.plot(years_slope, age_18_to_24_slope, color='#BFBEBE', label='18 to 24', linewidth=3.0)
ax.plot(years_slope, age_above_24_slope, color='#C3514E', label='Over 24', linewidth=3.0)

# Set title
ax.set_title('U.S. Overall Homeless By Age Group 2013-2020', loc='left')

# Make all spines invisible
ax.spines.right.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)

# Add scatter and text
ax.scatter(2013, 137242, s=40, color='#174A7E')
ax.text(2013, 147242, '137,242', color='#174A7E', ha='right')
ax.scatter(2020, 105524, s=40, color='#174A7E')
ax.text(2020, 115524, '105,524', color='#174A7E')

ax.scatter(2013, 59424, s=40, color='#BFBEBE')
ax.text(2013, 69424, '59,424', color='#BFBEBE', ha='right')
ax.scatter(2020, 44960, s=40, color='#BFBEBE')
ax.text(2020, 54960, '44,960', color='#BFBEBE')

ax.scatter(2013, 387817, s=40, color='#C3514E')
ax.text(2013, 397817, '387,817', color='#C3514E', ha='right')
ax.scatter(2020, 425200, s=40, color='#C3514E')
ax.text(2019.55, 435200, '425,200', color='#C3514E')

# Add annotation
ax.annotate('Homeless over the age of 24 is the only',
             xy=(2020, 425200),
             xytext=(2014.5, 340000),
             arrowprops=dict(arrowstyle='->', color='black',
                            connectionstyle='arc3, rad=0.15'),
             color='black')
ax.annotate('demographic to experience an increase ',
             xy=(2020, 425200),
             xytext=(2014.5, 320000),
             color='black')

# Set labels, limits, and ticks
ax.set_xlim(2012, 2021)
ax.set_xticks([2013, 2020])
ax.set_ylabel('People', color='black')
ax.set_yticks([])
ax.set_yticklabels([])

# The legend is plotted with four columns in the upper left of the plot with
# small fontsize and no frame
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
ax.legend(ncol=4, bbox_to_anchor=(0,1.015),
          loc='upper left', fontsize='small', frameon=False)

fig.tight_layout()
plt.show()
plot2b_filename = 'week_5_matplotlib_lyons_2_13JUN21.png'
fig.savefig(plot2b_filename, dpi=dpi)

 #%% Create DataFrame for third Matplotlib visual

# Read 'Overall Over 24' sheet from the
# '2007-2020-PIT-Estimates-by-state - Cleaned.xlsx" Excel workbook into
# 'df4' pandas DataFrame object
df4 = pd.read_excel(r'C:\Users\earle\Documents\GitHub\msds670_data_visualization\data\week_5\2007-2020-PIT-Estimates-by-state - Cleaned.xlsx', 
                    sheet_name='Overall Over 24')

# Create lists from DataFrame for the years and categories
over24_years = df4['Years'].tolist()
sheltered_individuals = df4['Sheltered Individuals'].tolist()
unsheltered_individuals = df4['Unsheltered Individuals'].tolist()
sheltered_families = df4['Sheltered People in Families'].tolist()
unsheltered_families = df4['Unsheltered People in Families'].tolist()
ca = df4['CA'].tolist()

 #%% Create the third Matplotlib visual

# Bar locations
x = np.arange(len(over24_years))
# Bar width
width = 0.20

# Create ax plot
fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x + 0.0, sheltered_individuals, width, color='#E6BAB7', label='Sheltered Individuals')
ax.bar(x + 0.2, ca, width, bottom=unsheltered_individuals, color='#94AFC5', label='CA Unsheltered Individuals')
ax.bar(x + 0.2, unsheltered_individuals, width, color='#C3514E', label='Unsheltered Individuals')
ax.bar(x + 0.4, sheltered_families, width, color='#BFBEBE', label='Sheltered Families')
ax.bar(x + 0.6, unsheltered_families, width, color='#A6A6A5', label='Unsheltered Families')

# Set text for title, labels, limits, and ticks
ax.set_title('U.S. Overall Homeless Over Age 24 2016-2020', loc='left')
ax.set_xticks(x + 0.3)
ax.set_xticklabels(over24_years)
ax.set_ylabel('People')
ax.set_ylim(0, 220000)
ax.set_yticks([])
ax.set_yticklabels([])

# Make all spines invisible
ax.spines.right.set_visible(False)
ax.spines.left.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.bottom.set_visible(False)

# Add text
ax.text(0.2, 138857, '136,857', color='black', ha='center')
ax.text(0.2, 35924, '52%', color='white', ha='center')
ax.text(0.2, 104352, '48%', color='black', ha='center')
ax.text(1.2, 152116, '150,116', color='black', ha='center')
ax.text(1.2, 37719, '50%', color='white', ha='center')
ax.text(1.2, 112777, '50%', color='black', ha='center')
ax.text(2.2, 158305, '156,305', color='black', ha='center')
ax.text(2.2, 40454, '52%', color='white', ha='center')
ax.text(2.2, 118606, '48%', color='black', ha='center')
ax.text(3.2, 178065, '176,065', color='black', ha='center')
ax.text(3.2, 41096, '47%', color='white', ha='center')
ax.text(3.2, 129128, '53%', color='black', ha='center')
ax.text(4.2, 191416, '189,416', color='black', ha='center')
ax.text(4.2, 45733, '48%', color='white', ha='center')
ax.text(4.2, 140441, '52%', color='black', ha='center')

# The legend is plotted with four columns in the upper left of the plot with
# small fontsize and no frame
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
ax.legend(ncol=5, bbox_to_anchor=(0,1.015),
          loc='upper left', fontsize='small', frameon=False)

fig.tight_layout()
plt.show()
plot3_filename = 'week_5_matplotlib_lyons_3_13JUN21.png'
fig.savefig(plot3_filename, dpi=dpi)