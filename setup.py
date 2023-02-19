#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='grobid_client_python',
      version='0.0.4',
      description='Python client for GROBID REST services',
      author='edumg180032',
      long_description=open("Readme.md", encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      url="https://github.com/edumg180032/IA-OS/grobid_client_python",
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=['requests'],
      entry_points={
          'console_scripts': ['grobid_client=grobid_client.grobid_client:main']
      },
      license='LICENSE',
    )
