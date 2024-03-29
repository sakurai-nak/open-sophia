# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx
import sphinx_rtd_theme
from sphinx.highlighting import lexers

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OpenSophia'
copyright = '2024-Present, Sakurai Nakatsuki, et al'
author = 'Nakatsuki S., et al'
release = '0.1b'
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_tabs.tabs",
    "notfound.extension",
    "sphinxext.opengraph",
    "sphinx_copybutton",
]

# Sphinx Tab Extension
sphinx_tabs_nowarn = True
sphinx_tabs_disable_tab_closing = True

# Not Found Extension
notfound_context = {
    "title": "Page not found",
    "body": """
        <h1>Page not found</h1>
        <p>
            Sorry, we couldn't find that page. It may have been renamed or removed
            in the version of the documentation you're currently browsing.
        </p>
        <p>
            If you're currently browsing the
            <em>latest</em> version of the documentation, try browsing the
            <a href="/en/stable/"><em>stable</em> version of the documentation</a>.
        </p>
        <p>
            Alternatively, use the
            <a href="#" onclick="$('#rtd-search-form [name=\\'q\\']').focus()">Search docs</a>
            box on the left or <a href="/">go to the homepage</a>.
        </p>
    """,
}

# OpenGraph Extension
ogp_site_name = "OpenSophia"

# Template
templates_path = ['_templates']
exclude_patterns = []
source_suffix = ".rst"
source_encoding = "utf-8-sig"

smartquotes = False
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
    "logo_only": True,
    "collapse_navigation": False,
    "display_version": False,
    "navigation_depth": -1,
}
html_title = "OpenSophia Knowledge Base Project"
html_static_path = ['_static']
html_css_files = [
    'css/algolia.css',
    'https://cdn.jsdelivr.net/npm/docsearch.js@2/dist/cdn/docsearch.min.css',
    "css/custom.css",
]
html_js_files = [
    "js/custom.js", # Increment the number at the end when the file changes to bust the cache.
]

# The master toctree document
master_doc = "index"