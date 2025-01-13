import os
import numpy as np
import open3d as o3d
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

print(f"Current working directory: {os.getcwd()}")


def load_obj_as_pointcloud(file_path):
    """
    Load an OBJ file and return its vertices as a point cloud.
    If the file cannot be loaded with Open3D, manually parse it.
    """
    try:
        print(f"Attempting to load OBJ file: {file_path}")
        mesh = o3d.io.read_triangle_mesh(file_path)
        if mesh.has_vertices():
            print("Vertices successfully loaded using Open3D.")
            return np.asarray(mesh.vertices)
        else:
            print("No vertices found using Open3D. Trying manual extraction.")
    except Exception as e:
        print(f"Open3D failed to load the file: {e}")

    # Manual extraction
    print("Manually extracting vertices...")
    return extract_vertices_from_obj(file_path)


def extract_vertices_from_obj(file_path):
    """
    Manually parse an OBJ file to extract vertices.
    Returns vertices as a NumPy array.
    """
    vertices = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):  # Vertex line
                    parts = line.split()
                    vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
        vertices = np.array(vertices)
        if vertices.size > 0:
            print(f"Extracted {len(vertices)} vertices manually.")
        else:
            print("No vertices found in the OBJ file.")
        return vertices
    except Exception as e:
        raise ValueError(f"Failed to manually parse the OBJ file: {e}")


def classify_shape(points, tolerance=0.1):
    """
    Classify points into a primary shape: sphere, cylinder, or cube.
    """
    # Normalize points
    centroid = np.mean(points, axis=0)
    points -= centroid

    # PCA for dimensionality reduction
    pca = PCA(n_components=3)
    pca.fit(points)
    explained_variance = pca.explained_variance_ratio_

    # Classify based on variance ratios
    if np.allclose(explained_variance, [1, 0, 0], atol=tolerance):
        return "Line"
    elif np.allclose(explained_variance, [0.5, 0.5, 0], atol=tolerance):
        return "Cylinder"
    elif np.allclose(explained_variance, [1/3, 1/3, 1/3], atol=tolerance):
        return "Sphere"
    else:
        return "Cube/Other"


def apply_dbscan_and_classify(points, eps=0.1, min_samples=10, tolerance=0.1):
    """
    Apply DBScan on point cloud and classify primary shapes.
    """
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    labels = dbscan.fit_predict(points)

    unique_labels = set(labels)
    shape_classes = {}

    for label in unique_labels:
        if label == -1:  # Noise points
            continue
        cluster_points = points[labels == label]
        shape = classify_shape(cluster_points, tolerance=tolerance)
        shape_classes[label] = shape

    return shape_classes


if __name__ == "__main__":
    # Specify the file path to the .obj file
    file_path = "bottle.obj"  # Replace with your file path

    # Check if the file exists
    if not os.path.exists(file_path):
        print("File not found. Please check the file path.")
    else:
        # Load the point cloud
        points = load_obj_as_pointcloud(file_path)

        if points is not None and points.size > 0:
            print(f"Loaded point cloud with {points.shape[0]} points.")
            # Apply DBSCAN and classify shapes
            shape_classes = apply_dbscan_and_classify(points, eps=0.2, min_samples=15)

            # Print classification results
            print("Shape classification results:")
            for label, shape in shape_classes.items():
                print(f"Cluster {label}: {shape}")
        else:
            print("Failed to load or extract points from the OBJ file.")
