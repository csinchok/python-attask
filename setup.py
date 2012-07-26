import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python-attask",
    version = "0.0.1",
    author = "Chris Sinchok",
    author_email = "csinchok@theonion.com",
    description = ("A Python API for ATTask"),
    license = "BSD",
    url = "http://gitlab.python.org/an_example_pypi_project",
    packages=['attask',],
    long_description=read('README.md'),
    install_requires = ['kombu>=2.3.0', 'isodate'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
