#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:    __init__
Author:  davidr
Created: 31.07.26 4:16 pm

"""
from importlib.metadata import version
from typing import TYPE_CHECKING
from collections.abc import Iterable
from ._utils import _load_package

if TYPE_CHECKING:
    import pandas as pd
    import polars as pl
    import numpy as np
    import numba as nb

    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    import anndata as ad
    import scanpy as sc
    import decoupler as dc
    import squidpy as sq
    import pertpy as pt
    import dotools_py as do

    import scvi



_aliases = {
    "pd": "pandas",
    "pl": "polars",
    "np": "numpy",
    "nb": "numba",

    "mpl":"matplotlib",
    "plt": "matplotlib.pyplot",
    "sns": "seaborn",

    "ad": "anndata",
    "sc": "scanpy",
    "do": "dotools_py",
    "dc": "decoupler",
    "sq": "squidpy",
    "scvi": "scvi",
    "pt": "pertpy",

}


def __getattr__(name: str) -> object:
    if name not in _aliases:
        raise AttributeError(f"module 'prelude_py' has no attribute '{name}'")
    module = _load_package(_aliases[name])
    globals()[name] = module
    return module

def __dir__() -> Iterable[str]:
    return sorted(list(globals()) + list(_aliases))

__all__ = tuple(_aliases.keys())
__version__ = version("prelude_py")
