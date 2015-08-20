#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Colin'
SITENAME = u'Colin go'
SITEURL = 'http://colinger.github.io'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('云极客', 'http://ycode.cn/'),)

# Social widget
SOCIAL = (('colinger@Github', 'https://github.com/colinge'),
          ('colingo@weixin', 'http://www.weibo.com/colingo/home'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Disqus
DISQUS_SITENAME = u"colinger"

# Content path
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']
# URL settings
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{base_name}/index.html'),
  (2, '{base_name}/page/', '{base_name}/page/{number}.html'),
)
ARTICLE_URL = ('articles/{slug}.html')
ARTICLE_SAVE_AS = ('articles/{slug}.html')
PAGE_LANG_SAVE_AS = False

# Feed
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Theme
THEME = 'pelican-themes/notmyidea-cms'
COVER_BG_COLOR = '#375152'
DEFAULT_PAGINATION = 10

# Plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap', 'gravatar' ]

# Sitemap
SITEMAP = {
  'format': 'xml',
  'priorities': {
    'articles': 1,
    'pages': 0.9,
    'indexes': 0.8,
  },
  'changefreqs': {
    'indexes': 'daily',
    'articles': 'daily',
    'pages': 'weekly'
  }
}

# Can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
