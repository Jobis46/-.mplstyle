# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx_gallery.sorting import ExampleTitleSortKey

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SciencePlots'
copyright = '2022, John D. Garrett'
author = 'John D. Garrett'
release = '2.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_gallery.gen_gallery'
]

templates_path = ['_templates']
exclude_patterns = []

# sphinx.ext.extlinks config
# External links aliases
repo_base_link = 'https://github.com/garrettj403/SciencePlots/'
extlinks = {
    'ghissue': (repo_base_link + 'issues/%s', 'issue %s'),
    'ghpull': (repo_base_link + 'pull/%s', 'pull request '),
    'ghwiki': (repo_base_link + 'wiki/%s', 'wiki '),
    'ghuser': ('https://github.com/%s', '@'),
    'doi': ('http://doi.org/%s', 'DOI: ')
}
# Warn replaceable hardcoded links
extlinks_detect_hardcoded_links = True

# sphinx.ext.autosectionlabel config
# prefix each section label with name of the doc it is in, followed by a colon
autosectionlabel_prefix_document = True
# sections for labeling by its depth
autosectionlabel_maxdepth = 2

# sphinx_gallery config
sphinx_gallery_conf = {
    'examples_dirs': '../../examples',  # path to example scripts
    'gallery_dirs': '_examples_autogenerated',  # generated output saving dir
    'run_stale_examples': True,  # rebuild all examples
    'nested_sections': True,
    'within_subsection_order': ExampleTitleSortKey,  # examples sorting order
    'filename_pattern': 'plot_.*\.py',
    'ignore_pattern': '__.*\.py',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom_sphinx_gallery.css',  # bigger size of thumbnails
]