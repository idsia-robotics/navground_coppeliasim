# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'navground_coppeliasim'
copyright = '2023, Jérôme Guzzi, IDSIA'
author = 'Jérôme Guzzi, IDSIA'
release = '0.6.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_tabs.tabs',
    'sphinxarg.ext',
    'sphinx_design',
    'sphinx_toolbox.collapse',
    'sphinxcontrib.luadomain',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/idsia-robotics/navground_coppeliasim",
    "repository_branch": "main",
    "path_to_docs": ""
}

toc_object_entries = True
toc_object_entries_show_parents = 'hide'
