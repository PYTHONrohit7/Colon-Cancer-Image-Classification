import logging
import os
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name
project_name = 'cnnClassifier'

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",  # Added .gitkeep for empty directory tracking in Git
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", # Assuming .ipynb extension for Jupyter notebooks
    "templates/index.html",
    "test.py"
]

# Loop through the list of files and create them
for filepath_str in list_of_files:
    filepath = Path(filepath_str) # Use Path object for better cross-platform compatibility
    filedir, filename = os.path.split(filepath) # os.path.split works well with Path objects too

    # Check if the directory part is not empty
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Create directory if it doesn't exist
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Check if the file does not exist OR if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create an empty file
        with open(filepath, "w") as f:
            pass # Just create the file, no need to write anything
        logging.info(f"Creating empty file: {filepath}")

    else:
        # Log if the file already exists and is not empty
        logging.info(f"{filename} already exists")

print("Project structure creation complete.")

