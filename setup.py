# setup.py

from setuptools import find_packages, setup

setup(
    name="parsdantic",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Sergi Fuster",
    author_email="sergifusterdura@gmail.com",
    description="This package provides a recursive function to convert json schemas to pydantic models.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SergiFuster/parsdantic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
