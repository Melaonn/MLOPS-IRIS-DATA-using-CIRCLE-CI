from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name = "mlopsmini1",
    version= "0.1",
    author="melson",
    packages=find_packages(),
    install_requires = requirements,
)