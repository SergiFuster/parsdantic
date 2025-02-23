# setup.py

from setuptools import find_packages, setup

setup(
    name="parsdantic",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Tu Nombre",
    author_email="tuemail@example.com",
    description="Una breve descripción de tu paquete",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SergiFuster/pydantizater",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
