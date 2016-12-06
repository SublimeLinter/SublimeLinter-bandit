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
from SublimeLinter.lint import util


class Bandit(PythonLinter):
    """Provides an interface to bandit."""

    syntax = 'python'
    cmd = ('bandit@python', '*', '-n', '1', '-f', 'txt', '-')
    version_args = '--version'
    version_re = r'^bandit\s(?P<version>\d+.\d+.\d+)'
    version_requirement = '>= 1.3.0'
    regex = (
        r'^>>\sIssue:\s\[.+\]\s(?P<message>.+)$\r?\n'
        r'^.*$\r?\n'
        r'^.*Location:.*:(?P<line>\d+)$\r?\n'
    )
    multiline = True
    error_stream = util.STREAM_BOTH
    config_file = ('--ini', '.bandit')
    defaults = {
        '--tests,': '',
        '--skips,': '',
    }
    inline_overrides = ('tests', 'skips')
