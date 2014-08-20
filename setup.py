#!/usr/bin/env python

from setuptools import setup, find_packages


def requirements():
    with open('./requirements.txt') as f:
        return [l.strip('\n') for l in f if l.strip('\n') and not l.startswith('#')]


print requirements()

setup(name='lrdatatypes',
      version='0.1',
      description='Provides core Land Registry data types to dependent applications',
      author='Land Registry',
      author_email='lr-dev@example.org',
      url='http://github.com/LandRegistry/audit-plugin',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      license='MIT',
      platforms='any',
      install_requires=['voluptuous', 'pycountry']
)
