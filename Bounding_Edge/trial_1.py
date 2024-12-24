import trimesh
import numpy as np
import matplotlib.pyplot as plt

# Load mesh
mesh = trimesh.load_mesh('plastic_water_bottle.obj')

for name, mesh in scene.geometry.items():
    print(f"Working with mesh: {name}")

    # Extract edges (will return a list of unique edges)
    #edges = mesh.edges_unique

    # Visualize the edges using Matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for edge in edges:
        v1 = mesh.vertices[edge[0]]
        v2 = mesh.vertices[edge[1]]
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], color='b', linewidth=0.5)

    plt.show()
