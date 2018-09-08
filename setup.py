from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

setup(
    name='connectfour',
    version='1.0.0',
    description='An implementation of the classic Connect Four game',
    author='Yanxi Chen',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='connectfour',
    packages=['connect4'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'connect4=connect4.connect4',
        ],
    },
)
