from setuptools import setup, find_packages

setup(
    name='GSON',
    version='1.0.0',
    description='Graph JSON file',
    author='Fadl Ghaddar',
    author_email='fadl2009gh@example.com',
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        'matplotlib',  # Add any dependencies your library requires
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
