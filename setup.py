#!/usr/bin/python3

from setuptools import setup

setup(
  name = 'eth_event',
  packages = ['eth_event'],
  version = '0.1',
  license = 'MIT',
  description = 'Ethereum event decoder and topic generator',
  author = 'Benjamin Hauser',
  author_email = 'ben.hauser@hyperlink.capital',
  url = 'https://github.com/iamdefinitelyahuman/eth-event',
  download_url = 'https://github.com/iamdefinitelyahuman/eth-event/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['ethereum'],
  install_requires=[            # I get to this in a second
          'eth-abi',
          'eth-hash',
          'hexbytes'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
) 
