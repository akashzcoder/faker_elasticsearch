import sys

from setuptools import find_packages, setup

if {"pytest", "test", "ptr"}.intersection(sys.argv):
    setup_requires = ["pytest-runner"]
else:
    setup_requires = []

setup(
    name="faker_elasticsearch",
    description="Fake data creation for Elasticsearch",
    version="1.0.0",
    author="Akash Singh",
    author_email="akashsingh.zcoder@gmail.com",
    setup_requires=setup_requires,
    license="none",
    packages=find_packages(),
)
