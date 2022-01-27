from setuptools import setup, find_packages

setup(
    name="blockchain-viewer",
    version="0.0.1",
    description="REST API for viewing Cosmos-based blockchains",
    author="Haja Florin-Gabriel",
    author_email="haja.fgabriel@gmail.com",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)
