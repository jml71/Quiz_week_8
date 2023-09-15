import pandas as pd
import matplotlib.pyplot as plt

csv_file = 'climate.csv'
data = pd.read_csv(csv_file)

years = data['Year']
temperatures = data['Temperature']


plt.figure(figsize=(10, 6)) 
plt.plot(years, temperatures, label='Temperature Data', marker='o', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Temperature')
plt.title('Temperature Data Over Time')
plt.legend()
plt.grid(True)

plt.show()
