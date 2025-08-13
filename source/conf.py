
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'SPECI'
author = 'Manting Mu', 'Timo Sommer', 'Max García-Melchor'
release = '1.0.0'

extensions = ['sphinx_rtd_theme', 'sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
