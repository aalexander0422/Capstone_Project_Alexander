import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('cardata.csv')

# Display basic statistics for numerical columns
print(data.describe())

# Display basic statistics for all columns
print(data.describe(include='all'))