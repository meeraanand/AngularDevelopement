import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("honey_1997.csv", header=0)
print(df['Value'])
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
print(df['Value'])      

all_honey = []
all_states = []
unique_states = [df['State']]
# without grouping
for state in unique_states:
    honey_data = (df[df['State'] == state])['Value']
    print (state, honey_data.sum())
    all_honey.append(honey_data.sum())
    all_states.append(state)
  
# with grouping
for state in unique_states:
    honey_data = df[df['State'] == state].groupby('Year')['Value']
    print (state, honey_data.sum())
    all_honey.append(honey_data.sum())
    all_states.append(state)

for i in range(5):
    honey = all_honey[i]
    state = all_states[i]  
    years = all_honey[i]
    
plt.plot(years, honey, label=state)