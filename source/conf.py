# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '565455手册'
copyright = '2025, FANCC'
author = 'FANCC'
release = '0.1.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'myst_parser', 'sphinx_copybutton']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "colon_fence",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
source_encoding = 'utf-8-sig'
html_search_language = 'zh'
html_search_options = {
    'type': 'default',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_theme_options = {
    'navigation_depth': 2,  # 控制导航栏的深度
    'collapse_navigation': False,  # 是否折叠导航栏
}
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]