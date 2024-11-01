from setuptools import setup, find_packages

setup(
    name="colorize_term",
    version="0.1",
    description="A simple library to add ANSI color codes to terminal text",
    long_description=open("README.md").read(),  # Optional, include your README for PyPI description
    long_description_content_type="text/markdown",
    author="Serber1990",
    author_email="serber1990@pm.me",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
