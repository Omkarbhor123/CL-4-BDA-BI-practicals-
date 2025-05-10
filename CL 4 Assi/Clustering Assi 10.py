
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target  # Actual labels (not used in clustering)

# Create a Pandas DataFrame
df = pd.DataFrame(data=X, columns=iris.feature_names)
df["species"] = y  # Add species labels

# Show first few rows of data
print("First 5 rows of the dataset:")
print(df.head())

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)
labels = kmeans.labels_

# Add cluster labels to DataFrame
df["Cluster"] = labels

# Reduce dimensions for visualization using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot clusters
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(pca.transform(kmeans.cluster_centers_)[:, 0], pca.transform(kmeans.cluster_centers_)[:, 1], c='red', marker='X', s=200, label="Centroids")
plt.title("K-Means Clustering on Iris Dataset")
plt.legend()
plt.show()
