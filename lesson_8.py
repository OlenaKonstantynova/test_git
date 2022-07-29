import numpy as np
import pandas as pd


b = np.arange(0, 50, 1)
print(b)
# np.random.random(size=(5, 5))

# np.random.randint()

print(b.argmin())
print(b.argmax())
print(b.size)
print(b.itemsize * b.size)
print(b.argsort())
print(b[b.argsort()])
x = np.random.randint(10, 100, size=20)
print(x)
print(np.median(x))
print(x.size)
print(np.percentile(x, 100))

# pandas

df = pd.read_csv('/Users/guest_here/Desktop/data.csv')
el = pd.DataFrame([{'element': 'Helium', 'symbol': 'He', 'atom`ic_number': 2}, {'element': 'Magnesium', 'symbol': 'Mg', 'atomic_number': 12}])
print(df.head(5))
print(df.tail(5))

print(df.describe())
#print(df.size())
print(df.shape)
print(df.columns)
print(df['price'].max)
print(df['bedrooms'].min)
print(df['bedrooms'].type)
print(pd.Series([1000, 2000, 3000], name='price', dtype=float))
education_s = pd.Series([1000, 2000, 3000, 40, 5000, 100000], name='price', dtype=float)
print(education_s)

print(education_s.shape)
print(education_s.max(), education_s.min(), education_s.std())

print(df.dtype)

df['city'] = df['city'].astype(str)
print(df.isna())
print(df['bedrooms'].isna())
print(df.isna().sum())
print(df.drop_duplicates('a'))
print(df.sort_values('bedrooms')[::-1])


print(df[df['price'] < 300000].head())

print(df[(df['bedrooms'] > 5) & (df['bathrooms'] > 1.5)].head(3))

print(df[(df['price'] < 500000) & (df['yr_build'] > '2001-01-01')].head(5))

print(df[(df['yr_build'] > '2001-01-01 00:00:00') & (df['price'] < 210000)].sort_values('price'))

print(df[(df['yr_build'] > '2001-01-01 00:00:00') & (df['price'] < 210000) & (df['price'] > 100000)].sort_values('price'))

print(df[(df['yr_built'] > 2001) & (df['price'] > 200000) & (df['bedrooms'] > 2) & (df['price'] < 500000)].head())

print(df[(df['bedrooms'] > 8) & (df['bedrooms'] < 10)])

print(df[(df['bedrooms'] > 8) & (df['bedrooms'] < 10)])
print(df['bedrooms'].value_counts())
