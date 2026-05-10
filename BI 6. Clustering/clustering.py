# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Create Dataset-- y =label is only  for testing visualization and comparision no training
X, y = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=1.0,
    random_state=42
)

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X)

    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8,5))

plt.plot(range(1,11), wcss, marker='o')

plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")

plt.show()

# Apply KMeans
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

# Train Model
y_kmeans = kmeans.fit_predict(X)

# Cluster Centers
centroids = kmeans.cluster_centers_

print("Centroids:\n")
print(centroids)

# Silhouette Score
score = silhouette_score(X, y_kmeans)

print("\nSilhouette Score:", score)

# Visualization
plt.figure(figsize=(8,6))

plt.scatter(
    X[:,0],
    X[:,1],
    c=y_kmeans
)

# Plot Centroids
plt.scatter(
    centroids[:,0],
    centroids[:,1],
    s=300,
    marker='X'
)

plt.title("K-Means Clustering")

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")

plt.show()