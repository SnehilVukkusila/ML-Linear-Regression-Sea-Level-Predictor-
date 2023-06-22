import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file

  # Use Pandas to import the data from epa-sea-level.csv
  df = pd.read_csv('epa-sea-level.csv')

  # Use matplotlib to create a scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Use the linregress function to get the slope and y-intercept of the line of best fit
  slope, intercept, rvalue, pvalue, stderr = linregress(
    df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create a range of x-values for the line of best fit
  x_values = range(1880, 2050)

  # Calculate the y-values for the line of best fit using the slope and y-intercept
  y_values = slope * x_values + intercept

  # Plot the line of best fit over the scatter plot
  plt.plot(x_values, y_values, 'r', label='Best fit line')

  # Predict sea level rise in 2050
  year_2050 = 2050
  sea_level_2050 = slope * year_2050 + intercept
  plt.scatter(year_2050,
              sea_level_2050,
              color='black',
              label='Prediction for 2050')

  # Plot a new line of best fit using the data from year 2000 through the most recent year in the dataset
  recent_data = df[df['Year'] >= 2000]
  slope_recent, intercept_recent, rvalue_recent, pvalue_recent, stderr_recent = linregress(
    recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
  x_values_recent = range(2000, 2050)
  y_values_recent = slope_recent * x_values_recent + intercept_recent
  plt.plot(x_values_recent,
           y_values_recent,
           'g',
           label='Best fit line from 2000')

  # Add labels and title to the plot
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  plt.legend()

  # Display the plot
  #plt.show()

  # Create scatter plot
  
  # Create first line of best fit

  # Create second line of best fit
  res2 = linregress(y2000_asarray, l2000_asarray)
      print(f"From the begining R-squared: {res2.rvalue**2:.6f}")
      year_ext_array2 = range(2000, 2050,1) # Extrapolated array from 2000 to 2050
    ax.plot(year_ext_array2, res2.intercept +res2.slope*year_ext_array2, 'r')
  # Add labels and title

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()