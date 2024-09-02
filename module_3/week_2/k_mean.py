from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt


class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k                   # Number of clusters
        self.max_iters = max_iters   # Maximum number of iterations
        self.centroids = None        # Coordinates of cluster centroids
        self.clusters = None         # Cluster assignment of each data point

    def initialize_centroids(self, data):
        """
        Randomly initialize cluster centroids
        Parameters:
            data (numpy.ndarray): input data to be clustered
        Return:
            None
        """
        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]

    def euclidean_distance(self, x1, x2):
        """
        Calculate the Euclidean distance between two data points
        Parameters:
            x1 (numpy.ndarray): data point 1
            x2 (numpy.ndarray): data point 2
        Return:
            float: Euclidean distance
        """
        return np.sqrt(np.sum(np.power(x1 - x2, 2)))

    def assign_clusters(self, data):
        """
        Assign clusters to data points
        Parameters:
            data (numpy.ndarray): input data to be clustered
        Return:
            numpy.ndarray: array containing the cluster of each data point
        """

        # Calculate the distance between each data point and the centroids using the euclidean_distance function
        distances = np.array([[self.euclidean_distance(x, centroid) for centroid in self.centroids] for x in data])

        # print(np.argmin(distances, axis=1)) # You can print this line to see how the allocation array is represented
        return np.argmin(distances, axis=1)

    def update_centroids(self, data):
        """
        Update cluster centroids
        Parameters:
            data (numpy.ndarray): input data to be clustered
        Return:
            numpy.ndarray: array containing the new cluster centroids
        """
        return np.array([data[self.clusters == i].mean(axis=0) for i in range(self.k)])

    def fit(self, data):
        """
        Training function
        Parameters:
            data (numpy.ndarray): input data to be clustered
        Return:
            None
        """
        # Call the method to randomly initialize cluster centroids
        self.initialize_centroids(data)
        self.plot_clusters(data, 0)

        for i in range(self.max_iters):
            # Assign clusters to the nearest data points
            self.clusters = self.assign_clusters(data)

            # Visualize clusters and centroids at this iteration
            self.plot_clusters(data, i)

            # Move the centroids to the center (mean) of their assigned clusters based on the data points
            new_centroids = self.update_centroids(data)

            # Stop if the centroids do not move
            if np.all(self.centroids == new_centroids):
                break

            # If centroids move, repeat the loop with new centroids
            self.centroids = new_centroids
            self.plot_clusters(data, i)

        # Plot the final result of clusters and centroids
        self.plot_final_clusters(data)

    def plot_clusters(self, data, iteration):
        """
        Plot clusters and centroids at each iteration
        Parameters:
            data (numpy.ndarray): input data to be clustered
            iteration (int): current iteration
        Return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title(f"Iteration {iteration + 1}")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

    def plot_final_clusters(self, data):
        """
        Plot the final clusters and centroids
        Parameters:
            data (numpy.ndarray): input data to be clustered
        Return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title("Final Clusters and Centroids")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()


if __name__ == "__main__":
    iris_dataset = load_iris()
    data = iris_dataset.data[:, :2]

    kmeans = KMeans(k=3, max_iters=100)
    kmeans.fit(data)