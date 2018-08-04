#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT LOCAL LIBRARIES
from .auto_docstring.docstring_builder import create_ultisnips_docstring
from . import config


config.setup()


__all__ = [
    'create_ultisnips_docstring',
]
