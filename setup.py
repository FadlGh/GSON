from setuptools import setup, find_packages

VERSION = '1'
DESCRIPTION = 'Graphing JSON files'

# Setting up
setup(
    name="GSON",
    version=VERSION,
    author="F4dL (Fadl Ghaddar)",
    author_email="fadl2009gh@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['matplotlib'],
    keywords=['python', 'video', 'graph', 'json'],
    classifiers=[
        "Development Status :: 1 - Publishing",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)