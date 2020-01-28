#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DEFAULT_DATE_FORMAT = "%d %B %Y"
DISPLAY_CATEGORIES_ON_MENU = False
DELETE_OUTPUT_DIRECTORY = True
LOCALE = "en_GB.utf8"

# Metadata
# ========

AUTHOR = 'Sébastien Brisard'
SITENAME = "Sébastien Brisard's blog"
SITEURL = "https://sbrisard.github.io"

PATH = 'content'
OUTPUT_PATH = ".."

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# URL settings
# ============

RELATIVE_URLS = False

# Feed settings
# =============

FEED_DOMAIN = SITEURL
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
TAG_FEED_ATOM = None

FEED_RSS = None
FEED_ALL_RSS = "feed.xml"
CATEGORY_FEED_RSS = None
AUTHOR_FEED_RSS = None
TAG_FEED_RSS = None

# Pagination
# ==========

DEFAULT_PAGINATION = False

# Themes
# ======

THEME = "themes/sb-simple"
LINKS = []
SOCIAL = []

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ("About this blog", "/pages/about.html"),
    ("About me", "https://cv.archives-ouvertes.fr/sbrisard"),
    ("Archives", "/archives.html"),
    ("GitHub", "https://github.com/sbrisard"),
    ("Twitter", "https://twitter.com/SebBrisard"),
    ("RSS", "feed.xml")]

SLUGIFY_SOURCE = 'basename'
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {"guess_lang": False, "css_class": "highlight"},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
