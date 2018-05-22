# coding: utf-8
try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import os
long_description = 'cryptowatch-client is a python client library for cryptowatch public market rest api'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name  = 'cryptowatch-client',
    version = '0.1.4',
    description = 'cryptowatch-client is a python client library for cryptowatch public market rest api',
    long_description = long_description,
    license = 'MIT',
    author = '10mohi6',
    author_email = '10.mohi.6.y@gmail.com',
    url = 'https://github.com/10mohi6/cryptowatch-api-python-client',
    keywords = 'cryptowatch',
    py_modules=['cryptowatch_client'],
    install_requires = ['requests'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Programming Language :: Python :: 3.6',
      'Intended Audience :: Financial and Insurance Industry',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Operating System :: OS Independent',
      'Topic :: Software Development :: Build Tools',
      'Topic :: Office/Business :: Financial :: Investment',
      'License :: OSI Approved :: MIT License'
    ]
)