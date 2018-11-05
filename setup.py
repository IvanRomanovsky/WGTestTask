from setuptools import setup, find_packages

required = [
    "pytest",
    "requests",
    "jsonschema"
]

setup(
    name='test_task',
    packages=find_packages(),
    install_requires=required
)