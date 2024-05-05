import datasets
import numpy as np

# Load the CodeSearchNet dataset.
codesearchnet_dataset = datasets.load_dataset("codesearchnet", data_files="codesearchnet")

# Load the Python Aiplatform main dataset.
aiplatform_dataset = datasets.load_dataset("github/python-aiplatform-main")

# Combine the datasets into a single dataset.
combined_dataset = np.concatenate([codesearchnet_dataset, aiplatform_dataset])

# Save the combined dataset to a file.
np.save("combined_dataset.npy", combined_dataset)
