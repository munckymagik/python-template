import os
import sys

root_folder = os.path.join(os.path.dirname(__file__), '..')
abs_root_folder = os.path.abspath(root_folder)
sys.path.insert(0, abs_root_folder)
