# Entry point for packaging and distributing the quickplots library.
# Install the package into your environment with:
#   pip install .
# or
#   python setup.py install
# You don’t run this in your analysis scripts; it’s for installation only.
from setuptools import setup, find_packages

setup(
    name="quickplots",
    version="0.1.0",
    author="Charlotte C",
    description="Convenient plotting classes for pandas with matplotlib and seaborn",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0",
        "matplotlib>=3.0",
        "seaborn>=0.11",
    ],
    python_requires='>=3.7',
)