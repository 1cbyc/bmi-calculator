"""
Setup script for BMI Calculator Pro
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bmi-calculator-pro",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A modern, feature-rich BMI calculator desktop application",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/1cbyc/bmi-calculator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: GTK",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "bmi-calculator=bmi:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md"],
    },
    keywords="bmi calculator health fitness desktop gui",
    project_urls={
        "Bug Reports": "https://github.com/1cbyc/bmi-calculator/issues",
        "Source": "https://github.com/1cbyc/bmi-calculator",
        "Documentation": "https://github.com/1cbyc/bmi-calculator#readme",
    },
) 