
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='pyppl_context',
    version='0.0.1',
    description='Upstream and downstream process reference for PyPPL',
    python_requires='==3.*,>=3.6.0',
    author='pwwang',
    author_email='pwwang@pwwang.com',
    license='MIT',
    entry_points={"pyppl": ["pyppl_context = pyppl_context"]},
    packages=[],
    package_dir={"": "."},
    package_data={},
    install_requires=['pyppl==3.*'],
    extras_require={"dev": ["pytest", "pytest-cov"]},
)
