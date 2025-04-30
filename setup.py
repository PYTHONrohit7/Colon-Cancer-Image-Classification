import setuptools

# Read the contents of your README file
# This will be used as the long description for your package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package version
__version__ = "0.0.0"

# --- Project Metadata ---
# These variables define essential information about your project
REPO_NAME = "Colon-Cancer-Image-Classification"
AUTHOR_USER_NAME = "PYTHONrohit7"
# SRC_REPO should match the name of your main source directory (e.g., 'cnnClassifier')
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "ronithpaliwal4@gmail.com"

# --- Setup Configuration ---
setuptools.setup(
    # The name of your package as it will appear on PyPI
    name=SRC_REPO,

    # The current version of your package
    version=__version__,

    # The author's name
    author=AUTHOR_USER_NAME,

    # The author's email address
    author_email=AUTHOR_EMAIL,

    # A short, one-sentence description of the package
    description="A small python package for a CNN based kidney disease classification app", # Slightly more descriptive

    # The long description read from the README file
    long_description=long_description,

    # Specifies the content type of the long description (usually Markdown)
    long_description_content_type="text/markdown", # Corrected content type key

    # The main URL for the project (usually the GitHub repository)
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    # Additional links related to the project (e.g., bug tracker, documentation)
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    # Specifies that the package source code is located in the 'src' directory
    # The empty string key "" indicates the root package directory maps to 'src'
    package_dir={"": "src"},

    # Automatically finds all packages (directories with __init__.py) within the 'src' directory
    packages=setuptools.find_packages(where="src")
)