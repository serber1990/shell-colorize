from setuptools import setup, find_packages

setup(
    name="shellcolorize",
    version="0.3",
    description="Add color to Linux CLI shell terminal output in ANSI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Serber1990",
    author_email="serber1990@pm.me",
    url="https://github.com/serber1990/shell-colorize",  # Link to your GitHub repository
    project_urls={
        "Bug Tracker": "https://github.com/serber1990/shell-colorize/issues",
        "Documentation": "https://github.com/serber1990/shell-colorize",
        "Source Code": "https://github.com/serber1990/shell-colorize",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
