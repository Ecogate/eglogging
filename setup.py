import os

from setuptools import setup

# path to the root eglogging directory
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# load the README for the "long description"
README_TEXT = ''
with open(os.path.join(BASE_PATH, 'README.md'), 'r') as fp:
  README_TEXT = fp.read()

VERSION = ''
with open(os.path.join(BASE_PATH, 'eglogging', 'VERSION'), 'r') as fp:
  VERSION = fp.read()

setup(
  name="eglogging",
  version=VERSION,
  description="Simple wrapper around the python logging module",
  long_description=README_TEXT,
  long_description_content_type="text/markdown",
  url="https://github.com/Ecogate/eglogging",
  author="Ecogate",
  author_email="eglogging@ecogate.com",
  license="MIT",
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
  ],
  packages=["eglogging"],
  include_package_data=True
)
