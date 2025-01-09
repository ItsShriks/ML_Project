import trimesh
import numpy as np
import matplotlib.pyplot as plt
import os
#print(os.getcwd())

# Load mesh
file_path = '/Users/shrikar/Library/Mobile Documents/com~apple~CloudDocs/Sem III/Machine Learning/Projects/ML_Project/Bounding_Edge/source-plastic_water_bottle/plastic_water_bottle.obj'
try:
    # Attempt to load the file
    scene = trimesh.load_mesh(file_path)
except Exception as e:
    print(f"Failed to load the file: {e}")
    exit()

if isinstance(scene, trimesh.Scene):
    print("The file contains multiple meshes. Processing each mesh individually.")
    for name, mesh in scene.geometry.items():
        print(f"Processing mesh: {name}")
        # Extract vertices and faces
        vertices = mesh.vertices
        faces = mesh.faces

        # Print surface information for this mesh
        print(f"  Number of vertices: {len(vertices)}")
        print(f"  Number of faces: {len(faces)}")
        for i, face in enumerate(faces[:5]):  # Limit output to first 5 faces
            v0, v1, v2 = vertices[face]
            print(f"  Face {i+1}:")
            print(f"    Vertex 1: {v0}")
            print(f"    Vertex 2: {v1}")
            print(f"    Vertex 3: {v2}")
else:
    print("The file contains a single mesh. Processing it.")
    mesh = scene  # Assign the Trimesh object to `mesh`
    vertices = mesh.vertices
    faces = mesh.faces

    # Print surface information
    print("Surface Information:")
    print(f"Number of vertices: {len(vertices)}")
    print(f"Number of faces: {len(faces)}")
    for i, face in enumerate(faces[:5]):  # Limit output to first 5 faces
        v0, v1, v2 = vertices[face]
        print(f"Face {i+1}:")
        print(f"  Vertex 1: {v0}")
        print(f"  Vertex 2: {v1}")
        print(f"  Vertex 3: {v2}")
        