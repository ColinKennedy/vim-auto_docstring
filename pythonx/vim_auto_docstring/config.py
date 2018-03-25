#!/usr/bin/env python
# -*- coding: utf-8 -*-

# IMPORT THIRD-PARY LIBRARIES
import auto_docstring
import vim


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


def setup():
    auto_docstring.register_config_entry('container_prefix', predicate=get_container_prefix)
    auto_docstring.register_config_entry('container_suffix', predicate=get_container_suffix)
    auto_docstring.register_config_entry('delimiter', predicate=get_delimiter)
    auto_docstring.register_config_entry('indent', predicate=get_indent)
    auto_docstring.register_config_entry('option_separator', predicate=get_option_separator)
    auto_docstring.register_config_entry('raw_prefix', predicate=get_raw_prefix)
    auto_docstring.register_config_entry('style', predicate=get_style)
    auto_docstring.register_config_entry('type_follow', predicate=allow_type_follow)
