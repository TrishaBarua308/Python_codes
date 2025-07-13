import random
from typing import List

class KMeans1D:
    def __init__(self, n_clusters: int, max_iter: int = 100, tolerance: float = 1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.centroids: List[float] = []
        self.labels: List[int] = []

    def _initialize_centroids(self, data: List[float]) -> List[float]:
        return random.sample(data, self.n_clusters)

    def _assign_clusters(self, data: List[float], centroids: List[float]) -> List[int]:
        labels = []
        for point in data:
            distances = [abs(point - c) for c in centroids]
            labels.append(distances.index(min(distances)))
        return labels

    def _compute_centroids(self, data: List[float], labels: List[int]) -> List[float]:
        new_centroids = [0.0] * self.n_clusters
        counts = [0] * self.n_clusters

        for point, label in zip(data, labels):
            new_centroids[label] += point
            counts[label] += 1

        for i in range(self.n_clusters):
            if counts[i] > 0:
                new_centroids[i] /= counts[i]

        return new_centroids

    def _has_converged(self, old_centroids: List[float], new_centroids: List[float]) -> bool:
        for old, new in zip(old_centroids, new_centroids):
            if abs(old - new) > self.tolerance:
                return False
        return True

    def fit(self, data: List[float]) -> None:
        self.centroids = self._initialize_centroids(data)

        for iteration in range(self.max_iter):
            self.labels = self._assign_clusters(data, self.centroids)
            new_centroids = self._compute_centroids(data, self.labels)

            if self._has_converged(self.centroids, new_centroids):
                print(f"[INFO] Converged at iteration {iteration + 1}")
                break

            self.centroids = new_centroids

    def predict(self, data: List[float]) -> List[int]:
        return self._assign_clusters(data, self.centroids)

    def print_results(self, data: List[float]) -> None:
        print("\nCluster Assignments:")
        for point, label in zip(data, self.labels):
            print(f"  Data Point: {point:.2f} -> Cluster {label}")

        print("\nFinal Centroids:")
        for i, c in enumerate(self.centroids):
            print(f"  Centroid {i}: {c:.4f}")

# ----------------------------
# Example Usage
# ----------------------------

if __name__ == "__main__":
    data = [1.2, 2.7, 3.1, 7.9, 9.5, 10.2, 11.3]
    kmeans = KMeans1D(n_clusters=2)
    kmeans.fit(data)
    kmeans.print_results(data)
