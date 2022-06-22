import os
import re
import sys
from pathlib import Path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='youtube',
    packages=['youtube'],
    author='Jie Jenn',
    author_email='jiejenn@learndataanalysis.org',
    version='1.0',
    keywords=['YouTube', 'YouTube Scraper'],
    python_requires='>=3.6',
    install_requires=['google-auth>=1.12.0', 'google-auth-oauthlib>=0.4.1'],
    license='MIT'
)    