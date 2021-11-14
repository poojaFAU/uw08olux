from distutils.core import setup
from setuptools import find_packages
setup(name='uw08olux',
      version='0.1',
      author='DSSS',
      author_email='pooja.basak@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])