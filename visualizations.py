import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'Selling_Price' is the correct column name in your dataset
data = pd.read_csv('cardata.csv')

def scatter(x, fig):
    plt.subplot(5, 2, fig)
    plt.scatter(data[x], data['Selling_Price'])
    plt.title(f'{x} vs Price')
    plt.ylabel('Price')
    plt.xlabel(x)

plt.figure(figsize=(10, 20))

scatter('Year', 1)
scatter('Kms_Driven', 2)  # Corrected column name

plt.tight_layout()
plt.show()