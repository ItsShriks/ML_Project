# Mixture-of-Gaussians for Object Recognition in Grasping Tasks

## Team Members
- Ayushi Arora
- Riddesh More
- Shrikar Nakhye
- Shubham Gawande

## Short Project Description
This project aims to utilize Mixture-of-Gaussians (MoG) models for object recognition in robotic grasping tasks. The process begins by gathering object data in the form of .obj files (vertex, texture, and face information). A systematic pipeline processes the data to extract meaningful features, identify basic geometric shapes, classify object categories, and apply the MoG model for further refinement.

By combining advanced clustering techniques with Expectation-Maximization (EM), this approach seeks to classify objects into fundamental categories such as cubes, cylinders, spheres, and cuboids. The robot will use this classification to adapt its grasping strategies for diverse object types.

## Workflow

### Step I: Data Collection

Use .obj files as input, containing vertices, vertex textures, and faces (e.g., [v, vt, f]).

### Step II: Pre-processing

Employ Open3D to:
- Extract bounding edges.
- Remove surface overlaps.
- Simplify object representations for efficient processing.

### Step III: Object Identification

Determine if a valid object exists within the dataset. Perform basic geometry checks to assess object completeness and structure.

### Step IV: Feature Extraction

Extract critical object features such as dimensions, curvature, and symmetry. Use these features to describe the object concisely for classification purposes.

### Step V: Category Classification
Classify objects into one of four predefined categories:
    1.	Cube
    2.	Cuboid
    3.	Cylinder
    4.	Sphere

### Step VI: Mixture-of-Gaussians (MoG) Application
Apply the MoG model for clustering based on object features. Use EM for optimizing the Gaussian parameters, ensuring high accuracy in category refinement.

### Step VII: Output Generation
Generate results in two forms:
    1. Image representations of the classified objects.
    2. Textual descriptions of the objects’ basic geometry.

### Step VIII: Validation

- Validate the classifications using predefined benchmarks and test objects.

## Learning Data
The dataset requirements include:
1.	Input Data: .obj files from sources such as ShapeNet.
2.	Pre-processed Features: Extracted object features like size and shape parameters.
3.	Labeled Data: Categories for cubes, cuboids, cylinders, and spheres, to train the model.

## Expected Project Outcomes
1.	A pipeline for preprocessing and classifying .obj files into basic geometric categories.
2.	A trained Mixture-of-Gaussians model capable of clustering objects based on extracted features.
3.	Integration of classification outputs with robotic grasping strategies for adaptive object manipulation.
## Evaluation Plan
The project’s success will be evaluated based on:
1.	Pipeline Accuracy: Precision of shape classification (cube, cylinder, etc.).
2.	Grasp Success Rate: Percentage of successful grasps based on classification output.
3.	System Generalization: Ability to handle unseen objects and maintain high classification accuracy.

## References
1.	Open3D: For pre-processing object geometry and feature extraction.
2.	ShapeNet Dataset: Repository of 3D object models.
3.	Mixture-of-Gaussians and EM Algorithms: Techniques for unsupervised clustering and parameter optimization.