#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='triforce',
    version='0.1.0',
    description='No-bullshit n-triples encoder/decoder',
    author='Station A',
    author_email='software@stationa.com',
    url='https://github.com/StationA/triforce',
    packages=find_packages(exclude=['*tests*']),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'triforce=triforce.__main__:main'
        ],
    },
    license='License :: OSI Approved :: MIT License',
)
