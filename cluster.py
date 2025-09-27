import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


data = pd.read_csv(r'C:\Users\pc44\Desktop\Exam 2025\Exam 2025\PART C\InsurancePrediction.csv')
print(data.head())
print(data.isnull().sum())


data = pd.get_dummies(data, columns=['FrequentFlyer'], drop_first=True)


print(data.columns)


features = data[['Age', 'FrequentFlyer_Yes', 'TravelInsurance']]


scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)


plt.plot(range(1, 11), wcss)
plt.title('Target Insurance Plan')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()


clusters = 4
kmeans = KMeans(n_clusters=clusters, init='k-means++', random_state=42)
y = kmeans.fit_predict(scaled_features)
print(y)
