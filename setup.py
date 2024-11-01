from setuptools import setup, find_packages

setup(
    name="colorize-term",
    version="0.2",
    description="A simple library to add ANSI color codes to terminal text",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Serber1990",
    author_email="serber1990@pm.me",
    url="https://github.com/serber1990/colorize-term",  # Link to your GitHub repository
    project_urls={
        "Bug Tracker": "https://github.com/serber1990/colorize-term/issues",
        "Documentation": "https://github.com/serber1990/colorize-term",
        "Source Code": "https://github.com/serber1990/colorize-term",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
