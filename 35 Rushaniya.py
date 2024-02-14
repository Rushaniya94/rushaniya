import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('flights')
correlation = df.pivot_table(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, cmap='coolwarm', annot=True, fmt='decimal')
plt.title('Luftgansa')

plt.show()

print(df)


import seaborn as sns
import matplotlib.pyplot as plt


tips= sns.load_dataset('tips')
sns.histplot(tips['total_bill'], color='blue',label='Total Bill', alpha=0.5)

plt.title('Bar graph common')
plt.xlabel('Meaning')
plt.ylabel('Range')

plt.show()