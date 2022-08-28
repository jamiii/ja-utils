# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ja-utils'
copyright = '2022, James Andrew'
author = 'James Andrew'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# auto api, https://sphinx-autoapi.readthedocs.io/en/latest/tutorials.html#setting-up-automatic-api-documentation-generation
extensions = ['autoapi.extension']
autoapi_dirs = ["../../ja-utils"]

html_logo = "../img/logo.png"

# -- Options for Theme, https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#
html_theme_options = {
    'logo_only': False,
    'display_version': True
    # 'style_nav_header_background': '#998129'
}