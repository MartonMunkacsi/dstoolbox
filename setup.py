from setuptools import setup, find_packages
import os
import sys

VERSION = '0.0.1' 
DESCRIPTION = 'A toolbox for Data Science.'
LONG_DESCRIPTION = 'A Data Science Toolbox with helpful functionality in preprocessing, data exploration and ML workflow.'

# Setting up
setup(
  name="dstoolbox", 
  version=VERSION,
  author="Marton Munkacsi",
  description=DESCRIPTION,
  long_description=LONG_DESCRIPTION,
  packages=find_packages(),
  install_requires=['pandas', 'numpy', 'spacy', 'scikit-learn'],
  keywords=['python', 'data science', 'toolbox', 'preprocessing', 'data exploration'],
  classifiers= [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Data Enthusiasts",
    "Programming Language :: Python :: 3",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
  ]
)

# Download en_core_web_sm model
if 'install' in sys.argv:
    os.system('python -m spacy download en_core_web_sm')