import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("GROUP 4")
st.header("Laptop Prices Dataset")

df = pd.read_csv("laptop_price.csv")

#Manalang 1

df.head(10)

nbins = int(np.sqrt(len(df)))

plt.figure(figsize=(10, 8))
plt.hist(df['Price (Euro)'], bins=nbins, edgecolor='black')

plt.title('Distribution of Laptop Prices', fontsize=12, fontweight='bold')
plt.xlabel('Price (Euro)')
plt.ylabel('Frequency')

st.pyplot(plt)

#Manalang 2

data = df['TypeName'].value_counts()

custom_order = ['Notebook', 'Gaming', 'Ultrabook', 'Netbook', '2 in 1 Convertible', 'Workstation']

data = data.reindex(custom_order).fillna(0)

color = ['#7AD9F8', '#A8D600', '#F15A5E', '#D46783', '#FFB84D', '#B47FC1']

explode = [0.05] * len(data)

plt.figure(figsize=(10, 8))
plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=40, colors=color, explode=explode, shadow=True, wedgeprops={'edgecolor':'black', 'linewidth' : 0.5, 'antialiased' : True})

plt.title('Distribution of Laptop Types', fontsize=12, fontweight='bold')

plt.axis('equal')
plt.show()

#Sunico 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Inches'], df['Price (Euro)'], color='blue', alpha=0.6, edgecolor='white',s=65)
ax.set_xlabel('Inches')
ax.set_ylabel('Price in Euros')
ax.set_title('Inches vs Price (Euro)', fontweight='bold')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.9)
ax.set_aspect(aspect='auto')
st.pyplot(plt)

#Sunico 2
df = pd.read_csv('laptop_price.csv')
company_counts = df['GPU_Company'].value_counts()

labels = company_counts.index
sizes = company_counts.values

colors = ['#00C7FD', '#76b900', '#ED1C24', '#0091BD'] #each of the hex codes are colors that each the companies use, you can barely see ARM but it also has a blue color.
explode = [0.05, 0.05, 0.05, 0.05]

plt.figure(figsize=(10, 9))
plt.pie(sizes, labels=labels, autopct='%0.2f%%', startangle=45, colors=colors, explode=explode, wedgeprops={'edgecolor':'black', 'linewidth' : 0.5, 'antialiased' : True}, shadow=True)
plt.axis('equal')
plt.title('Distribution of GPU Companies', fontsize=16, fontweight='bold')

st.pyplot(plt)

#Gonzales 1

average_prices = df.groupby('CPU_Company')['Price (Euro)'].mean().reset_index()

sns.set(style='whitegrid')

plt.figure(figsize=(16, 8))

cool_colors = {
    'AMD': 'red',
    'Intel': 'blue',
    'Samsung': 'purple'
}

colors = [cool_colors.get(company, 'lightgray') for company in average_prices['CPU_Company']]
bar_plot = sns.barplot(data=average_prices, x='Price (Euro)', y='CPU_Company', palette=colors)

plt.title('Average Laptop Prices by CPU Company', fontsize=20)
plt.xlabel('Average Price (Euro)', fontsize=16)
plt.ylabel('CPU Company', fontsize=16)

bar_plot.tick_params(axis='y', labelsize=12)
bar_plot.tick_params(axis='x', labelsize=12)

for index, value in enumerate(average_prices['Price (Euro)']):
    plt.text(value, index, f'€{value:.2f}', va='center', fontsize=12)

plt.show()

#Gonzales 2

plt.figure(figsize=(14, 8))
sns.boxplot(data=df, x='TypeName', y='Price (Euro)', palette='Set2')
plt.title('Price Distribution by Laptop Type', fontsize=20)
plt.xlabel('Type of Laptop', fontsize=16)
plt.ylabel('Price (Euro)', fontsize=16)
plt.xticks(rotation=45)


plt.show()