#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:    test_imports
Author:  davidr
Created: 31.07.26 4:36pm

Module description here.
"""
from prelude_py import pd, pl, np, nb, mpl, plt, sns, ad, sc, do, dc, sq, scvi, pt

def test_pandas():
    assert pd.__name__ == "pandas"

def test_polars():
    assert pl.__name__ == "polars"

def test_numpy():
    assert np.__name__ == "numpy"

def test_numba():
    assert nb.__name__ == "numba"

def test_matplotlib():
    assert mpl.__name__ == "matplotlib"

def test_matplotlib_pyplot():
    assert plt.__name__ == "matplotlib.pyplot"

def test_seaborn():
    assert sns.__name__ == "seaborn"

def test_anndata():
    assert ad.__name__ == "anndata"

def test_scanpy():
    assert sc.__name__ == "scanpy"

def test_dotools():
    assert do.__name__ == "dotools_py"

def test_decoupler():
    assert dc.__name__ == "decoupler"

def test_squidpy():
    assert sq.__name__ == "squidpy"

def test_scvi():
    assert scvi.__name__ == "scvi"

def test_pertpy():
    assert pt.__name__ == "pertpy"


def test_unknown():
    from prelude_py._utils import _load_package
    try:
        _load_package("unknown")
    except ImportError:
        pass

