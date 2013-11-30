#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '2xyo'
SITENAME = 'Pelican theme greyshade example'
SITEURL = 'http://pelican-theme-greyshade-example.yohann.lepage.info'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

STATIC_PATHS = ["images", ]

THEME = 'pelican-theme-greyshade'

# GRAVATAR
import hashlib
m = hashlib.md5()
m.update('me@example.com'.encode('utf-8'))
EMAIL_MD5 = m.hexdigest()
GRAVATAR_SIZE = 150 # 160px if not defined


# Links / icons
EMAIL = 'me@example.com'
GITHUB_USER = 'nickname'
FACEBOOK_USER = 'nickname'
GOOGLEPLUS_USER = '1234567890'
TWITTER_USER = 'getpelican'
CODERWALL_USER = "nickname"
STACKOVERFLOW_USER = "nickname"
STACKOVERFLOW_USER = 123456
LINKEDIN_USER = "nickname"
PINTEREST_USER = "hipster"
DELICIOUS_USER = "nickname"
PINBOARD_USER = "wtf"
DOUBAN_USER = "nickname"
SUBSCRIBE_FEED = True

