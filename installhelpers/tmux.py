from __future__ import print_function, unicode_literals, division

from .base import create_config_symlink, print_step


def configure(installation):
    print_step('Configuring tmux')
    create_config_symlink(installation, '.tmux.conf')
