#! /usr/bin/env python

import codecs
import os
import numpy as np

from setuptools import find_packages, setup
from setuptools.extension import Extension
from Cython.Build import cythonize

# get __version__ from _version.py
ver_file = os.path.join('skltree', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'scikit-tree'
DESCRIPTION = 'A minimal library implementing decision trees and tree ensembles.'
with codecs.open('README.rst', encoding='utf-8-sig') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'D. Herren'
MAINTAINER_EMAIL = 'drewherrenopensource@gmail.com'
URL = 'https://github.com/andrewherren/scikit-tree'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/andrewherren/scikit-tree'
VERSION = __version__
INSTALL_REQUIRES = ['numpy', 'scipy', 'scikit-learn', 'cython']
CLASSIFIERS = ['Intended Audience :: Science/Research',
               'Intended Audience :: Developers',
               'License :: OSI Approved',
               'Programming Language :: Python',
               'Topic :: Software Development',
               'Topic :: Scientific/Engineering',
               'Operating System :: Microsoft :: Windows',
               'Operating System :: POSIX',
               'Operating System :: Unix',
               'Operating System :: MacOS',
               'Programming Language :: Python :: 3.5',
               'Programming Language :: Python :: 3.6',
               'Programming Language :: Python :: 3.7']
EXTRAS_REQUIRE = {
    'tests': [
        'pytest',
        'pytest-cov'],
    'docs': [
        'sphinx',
        'sphinx-gallery',
        'sphinx_rtd_theme',
        'numpydoc',
        'matplotlib'
    ]
}

libraries = []
if os.name == "posix":
    libraries.append("m")

cython_extensions = [
    Extension(name = "skltree.tree._tree", sources = ["skltree/tree/_tree.pyx"], include_dirs = [np.get_include()], libraries = libraries, language = "c++", extra_compile_args = ["-O3"]), 
    Extension(name = "skltree.tree._splitter", sources = ["skltree/tree/_splitter.pyx"], include_dirs = [np.get_include()], libraries = libraries, extra_compile_args = ["-O3"]), 
    Extension(name = "skltree.tree._criterion", sources = ["skltree/tree/_criterion.pyx"], include_dirs = [np.get_include()], libraries = libraries, extra_compile_args = ["-O3"]), 
    Extension(name = "skltree.tree._utils", sources = ["skltree/tree/_utils.pyx"], include_dirs = [np.get_include()], libraries = libraries, extra_compile_args = ["-O3"]),
    Extension(name = "skltree.tree._random", sources = ["skltree/tree/_random.pyx"], include_dirs = [np.get_include()], libraries = libraries, extra_compile_args = ["-O3"]), 
]

setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      long_description=LONG_DESCRIPTION,
      ext_modules=cythonize(cython_extensions, compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
            "nonecheck": False,
            "cdivision": True,
      }), 
      zip_safe=False,  # the package can run out of an .egg file
      classifiers=CLASSIFIERS,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES,
      extras_require=EXTRAS_REQUIRE)