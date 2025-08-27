import seaborn as sns
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# df = sns.load_dataset('tips')
# sns.histplot(df['total_bill'], bins=30,kde=True, color='blue')
# plt.title("Total Bill Distribution")
# plt.show()

# data=pd.DataFrame({
#     "category":['A','B','C','D'],
#     "value":[4,7,2,9]
# })
# sns.barplot(x="category", y="value",data=data)
# plt.title("Normal Bar Chart (seaborn)")
# plt.show()


# df = sns.load_dataset('tips')
# sns.countplot(x="day", data= df, palette="Set2")
# plt.title("Count Plot")
# plt.show()

# df = sns.load_dataset('tips')
# sns.boxplot(x="day",y="total_bill", data= df, palette="pastel")
# plt.title("Box Plot")
# plt.show()

df = sns.load_dataset('tips')
sns.scatterplot(x="total_bill",y="tip", data= df, hue="sex" ,style="time")
plt.title("Scatter Plot")
plt.show()
