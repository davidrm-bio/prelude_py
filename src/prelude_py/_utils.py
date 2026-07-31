#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File:    _utils
Author:  davidr
Created: 31.07.26 4:32pm

Module description here.
"""
import importlib

def _load_package(name: str) -> object:
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError as e:
        raise ImportError(
            f"'{name}' is required but not installed\n"
            f"Install it with: pip install {name}"
        ) from e
