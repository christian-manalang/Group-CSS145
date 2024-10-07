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

st.write("The histogram illustrates that the frequency of laptop prices **peaks within the €0-€1,000 range**. Notably, while the **highest price for laptops approaches €6,000**, its frequency remains among the lowest. This indicates that laptops priced around **€1,000 are the most commonly found in the dataset**.")

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
st.pyplot(plt)

st.write("The histogram illustrates that the frequency of laptop prices **peaks within the €0-€1,000 range**. Notably, while the **highest price for laptops approaches €6,000**, its frequency remains among the lowest. This indicates that laptops priced around **€1,000 are the most commonly found in the dataset**.")
laptop_types = [
    "1. Notebook at 55.5%.",
    "2. Gaming at 16.1%.",
    "3. Ultrabook at 15.2%.",
    "4. 2 in 1 Convertible at 9.2%.",
    "5. Workstation at 2.3%.",
    "6. Netbook at 1.8%."
]

for laptop in laptop_types:
    st.write(laptop)

#Sunico 1
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df['Inches'], df['Price (Euro)'], color='blue', alpha=0.6, edgecolor='white',s=65)
ax.set_xlabel('Inches')
ax.set_ylabel('Price in Euros')
ax.set_title('Inches vs Price (Euro)', fontweight='bold')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.9)
ax.set_aspect(aspect='auto')
st.pyplot(plt)

st.write("This scatterplot shows the relationship between the inches of the laptop's screen and its price. "
         "Based on my observation, it seems that the larger a laptop's screen is, the more expensive it becomes. "
         "In this case, we can see how 10-inch laptops range below the 1000 euro mark, "
         "but 16.5-17 inch laptops can range from below 1000 to at most 6000 euros max.")

#Sunico 2
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

st.write("In this pie chart, we see the different companies which govern over the different GPU models of the laptops. "
         "All of the laptop GPUs are either owned by Intel, AMD, Nvidia, or even ARM, "
         "which has had a history of being bought out by Nvidia but has failed in recent years.")

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

st.pyplot(plt)

st.write("The bar graph shows the average price of laptops by CPU brand. Intel laptops are the most expensive at **1163.73€** on average. Samsung laptops are the second most expensive at **659€**, while AMD laptops are the cheapest at **560.99€**.")

#Gonzales 2

plt.figure(figsize=(14, 8))
sns.boxplot(data=df, x='TypeName', y='Price (Euro)', palette='Set2')
plt.title('Price Distribution by Laptop Type', fontsize=20)
plt.xlabel('Type of Laptop', fontsize=16)
plt.ylabel('Price (Euro)', fontsize=16)
plt.xticks(rotation=45)

st.pyplot(plt)

st.write("Through this box plot, we can see that ultrabooks and workstations are at the higher end of the price bracket, with median prices around **1500€** and **2000€** respectively. Gaming laptops show the most price variability, at times even extending beyond **4000€**. On the other hand, netbooks and notebooks are more budget-friendly, with median prices around **500€** and **800€**. The 2-in-1 convertibles offer moderate prices, with a median of **1000€**, and they also show less variation compared to other categories. Overall, gaming laptops and workstations are the most expensive, while netbooks and notebooks are the budget options.")

#Liandro1

plt.figure(figsize=(10, 6))
df['Company'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Count of Laptops by Company')
plt.xlabel('Company')
plt.ylabel('NUmber of Laptops')
plt.xticks(rotation=45)
st.pyplot(plt)

st.write("This bar chart displays the distribution of laptops by company, highlighting that **Dell**, **Lenovo**, and **HP** are the leading brands in the dataset, each contributing a significant number of laptops. **Asus** and **Acer** also have a notable presence, though smaller in comparison to the top three. Other brands like **Apple**, **MSI**, and **Toshiba** contribute fewer models, indicating a more focused product range or niche market targeting. The distribution suggests that Dell, Lenovo, and HP dominate the market with diverse offerings, while other brands cater to specific segments or premium categories.")

#Liandro2

plt.figure(figsize=(10, 6))
df['RAM (GB)'].value_counts().sort_index().plot(kind='barh', color='lightgreen')
plt.title('Count of Laptops by RAM Size')
plt.xlabel('Number of Laptops')
plt.ylabel('RAM (GB)')
st.pyplot(plt)

st.write("This horizontal bar chart shows the counts of laptops by RAM size, clearly illustrating that most of the laptops distributed are **8GB RAM**, followed by **4GB**, and finally **16GB**. Laptops with higher capacities, on the other hand, are much rarer. This suggests that most of the laptops distributed are geared towards everyday performance that doesn't require high RAM capacity.")

#DELA CRUZ CHARLES 1
storage_counts = df['Memory'].value_counts()

plt.figure(figsize=(15, 8))
sns.barplot(x=storage_counts.index, y=storage_counts.values)

plt.title('Distribution of Laptop Storage Configurations', fontsize=16)
plt.xlabel('Storage Configuration', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
for i, count in enumerate(storage_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.tight_layout()
st.pyplot(plt)
st.write("This bar chart shows the various distributions of laptop storage configurations and it clearly shows that the 256 SSD is the most prevalent among laptops followed by 1TB HDDs and 500 and 512 GB SSDs. This tells me that most of these laptops are willing to sacrifice storage size for increased read and write speeds. HDDs are also still prevalent as the graph shows HDD setups taking the 2nd and 3rd places. I also noticed many hybrid setups like the 128 GB SSD and the 1TB HDD that save costs by opting for a bigger 1TB HDD instead of a full SSD setup.")



#DELA CRUZ CHARLES 2

avg_prices = df.groupby('Company')['Price (Euro)'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
avg_prices.plot(kind='bar', color='skyblue')
plt.title('Average Laptop Prices by Company', fontsize=16)
plt.xlabel('Company', fontsize=12)
plt.ylabel('Average Price (Euro)', fontsize=12)
plt.xticks(rotation=45, ha='right')
for i, price in enumerate(avg_prices):
    plt.text(i, price, f'€{price:,.0f}', ha='center', va='bottom')
plt.tight_layout()
st.pyplot(plt)

st.write("This bar chart shows the average price each company on the dataset is charging for their laptops. Notably, Razer on average charged the highest at 3,346 Euro indicating that almost all of the Razer laptops in this dataset are high-spec and high-end laptops. Following Razer are LG, MSI, Google, Micosoft and Apple well known for their premium laptops. Huawei, Samsung, Toshiba, Dell, and Xiaomi have average laptop prices that can be considered mid-range. Asus, Lenovo, HP, Fujutsu, Acer, and the other brands are more budget oriented with average laptop prices at 1200 Eur and lowe")
