import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


customer_data = pd.read_csv("Mall_Customers.csv", encoding='latin1')
print(customer_data.head())
print(customer_data.isnull().sum())


le = LabelEncoder()


X = customer_data.iloc[:, [3, 4]].values
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


kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
Y = kmeans.fit_predict(X)

plt.figure(figsize=(8, 8))


plt.scatter(X[Y == 0, 0], X[Y == 0, 1], s=50, c='blue', label='Cluster 1')


plt.scatter(X[Y == 1, 0], X[Y == 1, 1], s=50, c='green', label='Cluster 2')


plt.scatter(X[Y == 2, 0], X[Y == 2, 1], s=50, c='red', label='Cluster 3')


plt.scatter(X[Y == 3, 0], X[Y == 3, 1], s=50, c='cyan', label='Cluster 4')


plt.scatter(X[Y == 4, 0], X[Y == 4, 1], s=50, c='magenta', label='Cluster 5')


plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            s=300, c='yellow', marker='*', label='Centroids')

plt.title("Customer Segments (KMeans Clustering)")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()
