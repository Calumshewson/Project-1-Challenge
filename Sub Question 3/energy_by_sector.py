import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Energy Consumption by Sector.csv')
plt.figure(figsize=(12, 8))
df.plot(x='State', kind='bar', stacked=True)

plt.title('Energy Consumption by Sector Across States')
plt.xlabel('State')
plt.ylabel('Energy Consumption')
plt.xticks(rotation=90)
plt.legend(title='Sectors')
plt.show()
