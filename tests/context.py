"""
This module is intended to provide common contextual setup/code for the tests
"""

import os
import sys

def _setup():
    root_folder = os.path.join(os.path.dirname(__file__), '..')
    abs_root_folder = os.path.abspath(root_folder)
    sys.path.insert(0, abs_root_folder)

_setup()
