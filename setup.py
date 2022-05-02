"""
Takeshi, robust background processing for Python.
"""
import os
from setuptools import find_packages, setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def get_version():
    basedir = os.path.dirname(__file__)
    try:
        with open(os.path.join(basedir, 'gesture/version.py')) as f:
            locals = {}
            exec(f.read(), locals)
            return locals['VERSION']
    except FileNotFoundError:
        raise RuntimeError('No version info found.')

setup(
    name='gesture',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    version=get_version(),
    url='https://github.com/orklann/gesture',
    description='Robust Background Processing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Aaron Elkins',
    author_email='threcius@yahoo.com',
    license='GPLv2.0',
    platforms='any'
)
