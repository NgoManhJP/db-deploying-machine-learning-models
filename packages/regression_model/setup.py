#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
from pathlib import Path

from setuptools import find_packages, setup


# Package meta-data.
NAME = 'regression_model'
DESCRIPTION = 'Train and deploy regression model.'
URL = 'your github project'
EMAIL = 'your_email@email.com'
AUTHOR = 'Your name'
REQUIRES_PYTHON = '>=3.6.0'


# このモジュールを実行するために必要なパッケージ?
def list_reqs(fname='requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()


# ------------------------------------------------
# ライセンスを変更する場合は、Trove Classifierを忘れずに変更！

here = os.path.abspath(os.path.dirname(__file__))

# READMEをインポートし、長い説明として使用します。
# 注：これは、MANIFEST.inファイルに「README.md」が存在する場合にのみ機能します！
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


# パッケージの__version__.pyモジュールを辞書としてロードします。
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'regression_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove分類子
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
