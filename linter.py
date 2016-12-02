#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Eric Brown
# Copyright (c) 2016 Eric Brown
#
# License: MIT
#

"""This module exports the Bandit plugin class."""

from SublimeLinter.lint import PythonLinter


class Bandit(PythonLinter):
    """Provides an interface to bandit."""

    syntax = 'python'
    cmd = ('bandit@python', '*', '-n 1', '-f txt', '-')
    #executable = None
    version_args = '--version'
    version_re = r'^bandit\s(?P<version>\d+.\d+.\d)'
    version_requirement = '>= 1.3.0'
    regex = (
        r'^>>\sIssue:\s\[.+\]\s(?P<message>.+)$\r?\n'
        r'^.*$\r?\n'
        r'^.*$\r?\n'
        r'^(?P<line>\d+)\s.*$\r?\n'
    )
    multiline = True
    #line_col_base = (1, 1)
    #tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    #selectors = {}
    #word_re = None
    #defaults = {}
    #inline_settings = None
    #inline_overrides = None
    #comment_re = None
    #module = 'bandit'
    #check_version = False
