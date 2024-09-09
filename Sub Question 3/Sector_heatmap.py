import pandas as pd
df = pd.read_csv('Energy Consumption by Sector.csv')
print(df.columns)

heatmap_data = df.set_index('State')
print(heatmap_data.head())

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 10))
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='.1f', linewidths=0.5)

plt.title('Energy Consumption by Sector Across States')
plt.xlabel('Sector')
plt.ylabel('State')
plt.tight_layout()
plt.show()

