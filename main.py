
import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv('cardata.csv')

# Display basic statistics for numerical columns
print(data.describe())

# Display basic statistics for all columns
print(data.describe(include='all'))


import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
data = pd.read_csv('cardata.csv')

# Display histograms for numerical attributes
numeric_columns = data.select_dtypes(include='number').columns

for column in numeric_columns:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[column], kde=True, color='skyblue')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

