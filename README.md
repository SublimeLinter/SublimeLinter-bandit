SublimeLinter-bandit
====================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [bandit](https://wiki.openstack.org/wiki/Security/Projects/Bandit). It will be used with files that have the “python” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `bandit` (1.3.0 or later) is installed on your system:

1. Install [Python](http://python.org/download/) and [pip](http://www.pip-installer.org/en/latest/installing.html).

1. Install `bandit` by typing the following in a terminal:
   ```
   [sudo] pip install bandit
   ```


In order for `bandit` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional settings for `bandit`:

- `tests`: comma-separated list of test IDs to run
- `skips`: comma-separated list of test IDs to skip
