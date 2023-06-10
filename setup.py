from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A toolbox for Data Science.'
LONG_DESCRIPTION = 'A Data Science Toolbox with helpful functionality in preprocessing, data exploration and ML workflow.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="dstoolbox", 
        version=VERSION,
        author="Marton Munkacsi",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'numpy', 'spacy', 'scikit-learn'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'data science', 'toolbox', 'preprocessing', 'data exploration'],
        classifiers= [
            "Development Status :: 1 - Planning",
            "Intended Audience :: Data Enthusiasts",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)