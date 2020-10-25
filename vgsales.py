import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 12)

data = pd.read_csv('E:/.../vgsales.csv')

print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())

datacorr = data[['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
sns.heatmap(datacorr.corr(), annot=True)
plt.show()

sns.countplot(x='Genre', data=data, order=data['Genre'].value_counts().index)
plt.title('genre distribution')
plt.xticks(rotation=45)
plt.show()

sns.countplot(x='Year', data=data, order=data['Year'].value_counts().index)
plt.title('year distribution')
plt.xticks(rotation=45)
plt.show()

sns.countplot(x='Platform', data=data, order=data['Platform'].value_counts().index)
plt.title('platform distribution')
plt.xticks(rotation=45)
plt.show()

topnasales = data.sort_values(by='NA_Sales', ascending=False).head()
sns.barplot(x='Name', y='NA_Sales', data=topnasales)
plt.title('top 5 games by NA_Sales')
plt.xticks(rotation=45)
plt.show()

topeusales = data.sort_values(by='EU_Sales', ascending=False).head()
sns.barplot(x='Name', y='EU_Sales', data=topeusales)
plt.title('top 5 games by EU_Sales')
plt.xticks(rotation=45)
plt.show()

topjpsales = data.sort_values(by='JP_Sales', ascending=False).head()
sns.barplot(x='Name', y='JP_Sales', data=topjpsales)
plt.title('top 5 games by JP_Sales')
plt.xticks(rotation=45)
plt.show()

topothsales = data.sort_values(by='Other_Sales', ascending=False).head()
sns.barplot(x='Name', y='Other_Sales', data=topothsales)
plt.title('top 5 games by Other_Sales')
plt.xticks(rotation=45)
plt.show()

topglsales = data.sort_values(by='Global_Sales', ascending=False).head()
sns.barplot(x='Name', y='Global_Sales', data=topglsales)
plt.title('top 5 games by Global_Sales')
plt.xticks(rotation=45)
plt.show()

mostgenreeachyear = data.groupby(['Year', 'Genre']).size().reset_index().sort_values(by=0, ascending=False).drop_duplicates(subset='Year', keep='first')
mostgenreeachyear.rename(columns={0:'counts'}, inplace=True)
print(mostgenreeachyear)

plt.figure(figsize=(12,5))
plot1 = sns.barplot(x='Year', y='counts', data=mostgenreeachyear, hue='Genre', dodge=False, order=mostgenreeachyear['Year'])
for p in plot1.patches:
    plot1.annotate(format(p.get_height(), '.0f'),
                   (p.get_x() + p.get_width() / 2, p.get_height()),
                   ha = 'center', va = 'center',
                   size=9,
                   xytext = (0, 5),
                   textcoords = 'offset points')
plt.xticks(rotation=90)
plt.show()

globalsalesyear = data.groupby('Year')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
sns.barplot(x='Year', y='Global_Sales', data=globalsalesyear, order=globalsalesyear['Year'])
plt.title('global sales each year')
plt.xticks(rotation=90)
plt.show()

mostplateachyear = data.groupby(['Year', 'Platform']).size().reset_index().sort_values(by=0, ascending=False).drop_duplicates(subset='Year', keep='first')
mostplateachyear.rename(columns={0:'counts'}, inplace=True)
sns.barplot(x='Year', y='counts', data=mostplateachyear, hue='Platform', order=mostplateachyear['Year'], dodge=False)
plt.xticks(rotation=90)
plt.show()

pubyear = data.groupby(['Year', 'Publisher']).size().sort_values(ascending=False).reset_index().drop_duplicates(subset='Year', keep='first')
pubyear.rename(columns={0:'counts'}, inplace=True)
sns.barplot(x='Year', y='counts', data=pubyear, hue='Publisher', order=pubyear['Year'], dodge=False)
plt.title('most publisher per year')
plt.xticks(rotation=90)
plt.show()

salescomparegenre = data.groupby('Genre')['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'].sum()
sns.heatmap(salescomparegenre, annot=True, fmt='.1f')
plt.title('sales comparison each genre')
plt.show()

salescompareplatform = data.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
sns.barplot(x='Platform', y='Global_Sales', data=salescompareplatform)
plt.title('sales comparison each platform')
plt.ylabel('global sales in $')
plt.xticks(rotation=45)
plt.show()


print(data.describe())
print(data.head())
print(data.info())

