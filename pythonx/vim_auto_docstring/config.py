#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT THIRD-PARY LIBRARIES
import vim

# IMPORT LOCAL LIBRARIES
from .auto_docstring.config import environment


def get_vim_style():
    return vim.eval('g:auto_docstring_style')


def get_container_prefix():
    return vim.eval('g:auto_docstring_container_prefix')


def get_container_suffix():
    return vim.eval('g:auto_docstring_container_suffix')


def get_delimiter():
    return vim.eval('g:auto_docstring_delimiter')


def get_indent():
    return vim.eval('g:auto_docstring_indent')


def get_option_separator():
    return vim.eval('g:auto_docstring_option_separator')


def get_raw_prefix():
    return vim.eval('g:auto_docstring_raw_prefix')


def get_style():
    return vim.eval('g:auto_docstring_style')


def allow_type_follow():
    return vim.eval('g:auto_docstring_type_follow')


def get_description_separator():
    return vim.eval('g:auto_docstring_description_separator')


def setup():
    environment.register_config_entry('container_prefix', predicate=get_container_prefix)
    environment.register_config_entry('container_suffix', predicate=get_container_suffix)
    environment.register_config_entry('delimiter', predicate=get_delimiter)
    environment.register_config_entry('indent', predicate=get_indent)
    environment.register_config_entry('option_separator', predicate=get_option_separator)
    environment.register_config_entry('raw_prefix', predicate=get_raw_prefix)
    environment.register_config_entry('style', predicate=get_style)
    environment.register_config_entry('type_follow', predicate=allow_type_follow)
    environment.register_config_entry('description_separator', predicate=get_description_separator)
