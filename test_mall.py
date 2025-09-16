import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

customer_data=pd.read_csv("Mall_Customers.csv", encoding='latin1')
print(customer_data.head())
print(customer_data.isnull().sum())
le=LabelEncoder()

X=customer_data.iloc[:, [3, 4]].values
print(X)

wcss = []  

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)                 
    wcss.append(kmeans.inertia_)  

plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Inertia)')
plt.show()
