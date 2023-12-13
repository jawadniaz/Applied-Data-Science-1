# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:16:15 2023

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt

# Replace this with the actual path to your CSV file
file_path = '/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select countries and indicators of interest
selected_countries = ['Bhutan', 'Fiji', 'India', 'Thailand', 'South Africa']
selected_indicators = ['Access to electricity (% of population)', 'Agricultural land (% of land area)']

# Filter data for selected countries and indicators
selected_data = data[(data['Country Name'].isin(selected_countries)) & (data['Indicator Name'].isin(selected_indicators))]

# Set up bar positions and width
bar_positions = range(len(selected_countries))
bar_width = 0.35

# Create subplots
fig, ax = plt.subplots()

# Plot bars for each indicator and country
for i, indicator in enumerate(selected_indicators):
    for j, country in enumerate(selected_countries):
        subset_data = selected_data[(selected_data['Country Name'] == country) & (selected_data['Indicator Name'] == indicator)]
        ax.bar(bar_positions[j] + i * bar_width, subset_data.iloc[0, 2:], width=bar_width, label=f'{country} - {indicator}')

# Set labels and title
ax.set_xticks([pos + bar_width / 2 for pos in bar_positions])
ax.set_xticklabels(selected_countries)
ax.set_xlabel('Country')
ax.set_ylabel('Indicator Value')
ax.set_title('Bar Chart for Selected Indicators and Countries')

# Add legend
ax.legend()

# Show the plot
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Agricultural land (% of land area)', 'Access to electricity (% of population)']

# Select the specific country for analysis
selected_country = 'South Africa'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select specific indicators for analysis
indicators_to_analyze = ['Agricultural land (% of land area)', 'Access to electricity (% of population)']

# Select the specific country for analysis
selected_country = 'Thailand
'

# Filter data for selected indicators and country
selected_data = data[(data['Indicator Name'].isin(indicators_to_analyze)) & (data['Country Name'] == selected_country)]

# Plot time trends for the selected country and indicators
plt.figure(figsize=(16, 10))
for indicator in indicators_to_analyze:
    indicator_data = selected_data[selected_data['Indicator Name'] == indicator]
    plt.plot(indicator_data.columns[2:], indicator_data.iloc[0, 2:], label=indicator)

plt.xlabel('Year')
plt.ylabel('Value')
plt.title(f'Time Trends for {selected_country} - Selected Indicators')
plt.legend()

# The y-axis limits are determined automatically

plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Access to electricity (% of population)', 'Agricultural land (% of land area)']
selected_country = 'India'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the vertical bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar_positions = range(len(years))
bar1 = plt.bar(bar_positions, values1, width=bar_width, label=indicators_to_plot[0], color='red')
bar2 = plt.bar(bar_positions, values2, width=bar_width, label=indicators_to_plot[1], color='black', bottom=values1)

plt.title(f'{selected_country} - Agricultural Land and Forest Area (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(bar_positions, years)  # Set the x-axis ticks to represent years
plt.legend()
plt.grid(axis='y')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select data for the specific indicators and country
indicators_to_plot = ['Access to electricity (% of population)', 'Agricultural land (% of land area)']
selected_country = 'Fiji'

# Filter data
selected_data = data[(data['Country Name'] == selected_country) & (data['Indicator Name'].isin(indicators_to_plot))]

# Extract years and values for the bar chart
years = selected_data.columns[2:]
values1 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[0]].iloc[0, 2:]
values2 = selected_data[selected_data['Indicator Name'] == indicators_to_plot[1]].iloc[0, 2:]

# Plot the clustered column chart
plt.figure(figsize=(12, 8))
bar_width = 0.35
bar_positions1 = [pos - bar_width/2 for pos in range(len(years))]
bar_positions2 = [pos + bar_width/2 for pos in range(len(years))]

bar1 = plt.bar(bar_positions1, values1, width=bar_width, label=indicators_to_plot[0], color='Green')
bar2 = plt.bar(bar_positions2, values2, width=bar_width, label=indicators_to_plot[1], color='Orange')

plt.title(f'{selected_country} - Agricultural Land and Forest Area (1990-2020)')
plt.xlabel('Year')
plt.ylabel('Values')
plt.xticks(range(len(years)), years)  # Set the x-axis ticks to represent years
plt.legend()
plt.grid(axis='y')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Access to electricity (% of population)', 'Agricultural land (% of land area)']

# Filter data for selected indicators
selected_data = data[data['Indicator Name'].isin(selected_indicators)]

# Pivot the data
pivot_data = selected_data.pivot(index='Country Name', columns='Indicator Name', values='2000')

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title('Correlation Matrix for Selected Indicators 2000')

# Show the plot
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/Climate Indicators.csv'
data = pd.read_csv(file_path)

# Select specific indicators for correlation matrix
selected_indicators = ['Access to electricity (% of population)', 'Agricultural land (% of land area)']

# Filter data for selected indicators
selected_data = data[data['Indicator Name'].isin(selected_indicators)]

# Pivot the data
pivot_data = selected_data.pivot(index='Country Name', columns='Indicator Name', values='2020')

# Create a correlation matrix for selected indicators
correlation_matrix = pivot_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Draw the heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

# Set the title
plt.title('Correlation Matrix for Selected Indicators 2020')

# Show the plot
plt.show()