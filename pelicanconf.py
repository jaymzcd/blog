#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alessandro De Noia'
SITENAME = u"Sdonk's blog"
TAGLINE= u"A place to collect my thoughts"
SITEURL = 'http://sdonk.org'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
}

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Social widget
SOCIAL = (('github', 'https://github.com/sdonk'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = './theme'

TWITTER_USERNAME = 'sdonk'

TYPOGRIFY  = True

#
STATIC_PATHS = ['images']

DISQUS_SITENAME = 'sdonk'



USER_LOGO_URL = SITEURL + '/static/images/me.png'