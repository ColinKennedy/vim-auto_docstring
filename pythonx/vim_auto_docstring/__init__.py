#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT THIRD-PARTY LIBRARIES
import vim

# IMPORT THIRD-PARTY LIBRARIE
from auto_docstring.docstring_builder import create_ultisnips_docstring

# IMPORT LOCAL LIBRARIES
from . import config


config.setup()


__all__ = [
    'create_ultisnips_docstring',
]
