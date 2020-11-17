import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv("honey.csv", header=0)
print(df['Value'])
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
print(df['Value'])

unique_states = df['State'].unique()
all_honey = []
all_states = []
  
# with grouping
for state in unique_states:
    honey_data = df[df['State'] == state].groupby('Year')['Value']
    print (state, honey_data.sum())
    all_honey.append(honey_data.sum())
    all_states.append(state)

for i in range(len(all_honey)-1):
    honey = all_honey[i]
    state = all_states[i]
    years = all_honey[i].keys() 
    plt.plot(years, honey, label=state) 

plt.show()       
    