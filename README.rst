.. -*- mode: rst -*-

scikit-tree
------------

**scikit-tree** is a project designed to make experimentation with tree-based machine learning methods straightforward. 
It relies on, and extends, the tree code in ``scikit-learn``.

Installation
------------

This project is currently brand new and not yet available on PyPI or conda-forge. 
The only way to install is to build the source package, as detailed below.

Installing from source
~~~~~~~~~~~~~~~~~~~~~~

Building scikit-tree from the Github source largely follows the instructions given in scikit-learn's 
"`advanced installation <https://scikit-learn.org/stable/developers/advanced_installation.html#platform-specific-instructions>`_" 
instructions. For MacOS and Linux this can be accomplished by installing python dependencies, compilers, and C/C++ dependencies into 
a conda environment via conda-forge::

    conda create -n partition_env -c conda-forge python=3.10 numpy scipy cython pytest matplotlib pandas \
        joblib threadpoolctl pytest compilers llvm-openmp
    
    conda activate partition_env
    
    cd ~/[path to folder]/scikit-tree
    python setup.py clean
    pip install --no-build-isolation -e .


Getting Started
---------------

The easiest way to get up and running with scikit-tree, once installed as above, is to run a script provided in the ``examples`` subfolder of the project. For example::

    conda activate partition_env
    cd ~/[path to folder]/scikit-tree
    python -m examples.tree.plot_regression_tree

