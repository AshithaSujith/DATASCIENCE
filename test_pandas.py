import pandas as pd
# s= pd.Series([10, 20, 30, 40])
# print(s)

# data={'name':['Alice','Bob'],'Age':[25,30]}
# df=pd.DataFrame(data)
# print(df)

data={'Name':['Alice','Bob','Charlie','David','Eva','Frank'],
      'score':[85,90,78,92,88,75],
}
df=pd.DataFrame(data)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(3))
df.info()
print(df.describe())
print(df.columns)
print(df.shape)