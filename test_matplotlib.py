import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# x= np.linspace(0,30,200)
# y=np.sin(x)
# plt.plot(x,y,color='black',linestyle='--',marker='o')
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

# x=np.random.rand(50)
# y=np.random.rand(50)
# plt.scatter(x,y,color='blue',marker='o')
# plt.title("Scatter Plot")
# plt.show()

# categories=['A','B','C']
# values=[3,7,5]
# plt.bar(categories,values,color=['red','green','blue'])
# plt.title("Bar Plot")
# plt.show()

# categories=['A','B','C']
# values=[3,7,5]
# plt.barh(categories,values,color='purple')
# plt.title("Bar Plot")
# plt.show()

# data=np.random.randn(1000)
# plt.hist(data,bins=30,color='skyblue',edgecolor='black')
# plt.title("Histogram")
# plt.show()

# sizes=[20,30,25,25]
# labels=['A','B','C','D']
# plt.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
# plt.title("Pie Chart")
# plt.show()

# days=[1,2,3,4,5]
# sleeping=[7,8,6,11,7]
# eating=[2,3,4,3,2]
# working=[7,8,7,2,2]
# playing=[8,5,7,8,13]
# plt.stackplot(days,sleeping,eating,working,playing,labels=['Sleep','Eat','Work','Play'],colors=['red','blue','pink','violet'])
# plt.legend(loc='upper left')
# plt.title("Stacked Area Plot")
# plt.show()

data=np.random.normal(100,20,200)
plt.boxplot(data)
plt.title("Box Plot")
plt.show()