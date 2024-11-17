# Mixture-of-Gaussians for Object Recognition in Grasping Tasks

## Team Members
- Ayushi Arora
- Riddesh More
- Shrikar Nakhye
- Shubham Gawande

## Short Project Description
This project focuses on utilizing Mixture-of-Gaussians (MoG) models to enable a robot to recognize and classify objects for adaptive grasping. Object recognition plays a critical role in robotic manipulation, particularly in scenarios involving diverse objects with varying shapes, sizes, and materials. The MoG model will be applied to cluster objects based on sensor data (visual or tactile), enabling the robot to determine the most appropriate grasp strategy for each object type.

## Learning Techniques
The project will use the Mixture-of-Gaussians (MoG) approach combined with Expectation-Maximization (EM) for clustering object types. Sensor data (e.g., RGB-D images or tactile readings) will be used for feature extraction, which is essential for identifying characteristics such as shape, texture, and material properties. The MoG model will be trained to segment objects into distinct categories, aiding in classification and decision-making for grasping.

## Learning Data
The dataset requirements for this project include:
1. **Diverse Object Types**: A collection of objects that vary in shape, size, texture, and material. These should represent real-world items the robot may encounter.
2. **Visual Features**: RGB-D images or 3D point clouds to capture geometric and color-based object characteristics.
3. **Tactile Features** (if available): Data from tactile or force/torque sensors to provide information on surface properties, stiffness, and material.
4. **Labeled Data**: Each object must be annotated with a category or class label to train the MoG model for clustering.

Initial datasets such as **ShapeNet** (for 3D object models) and **Google’s Object Dataset** (for annotated images) will be used. Additional dataset augmentation may be performed to improve model robustness and account for variability in object properties.

## Expected Project Outcomes
1. A Mixture-of-Gaussians model capable of clustering objects into meaningful categories based on sensor data.
2. A system that integrates object recognition with grasping strategies, enabling adaptive manipulation of objects.
3. A comprehensive library of clustered object data and corresponding grasping strategies, demonstrating the model’s ability to generalize to new objects.

## Evaluation Plan
The success of the project will be measured by:
1. **Classification Accuracy**: How effectively the MoG model clusters objects into correct categories.
2. **Grasp Success Rate**: The percentage of successful grasps across diverse object types, demonstrating the robot’s ability to adapt its grasping strategy based on object classification.
3. **Generalization**: The model’s performance on unseen objects, reflecting its robustness and adaptability.

## References
1. **ShapeNet Dataset**: A large-scale repository of 3D models categorized by type.
2. **Google’s Object Dataset**: Provides annotated images across a wide range of object classes.
3. Research literature on Mixture-of-Gaussians and Expectation-Maximization for clustering in robotic object recognition tasks.
