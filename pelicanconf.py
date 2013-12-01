#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '2xyo'
SITENAME = 'Pelican theme greyshade example'
SITEURL = 'http://pelican-theme-greyshade-example.yohann.lepage.info'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


BLOG_URL = '/'
BLOG_INDEX_SAVE_AS = 'index.html'


ARTICLE_DIR = 'blog'
ARTICLE_URL = "/blog/{date:%Y}/{date:%m}/{slug}"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}.html"

PAGE_DIR = 'pages'
PAGE_URL = '/pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'

CATEGORY_URL = '/blog/categories/{slug}'
CATEGORY_SAVE_AS = 'blog/categories/{slug}.html'

TAG_URL = '/blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}.html'
TAGS_URL = '/blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

AUTHOR_URL = '/blog/authors/{slug}'
AUTHOR_SAVE_AS = 'blog/authors/{slug}.html'
AUTHORS_URL = '/blog/authors'
AUTHORS_SAVE_AS = 'blog/authors.html'

ARCHIVES_SAVE_AS = 'blog/archives.html'

STATIC_PATHS = [
	'images',
    'extra/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    }

PLUGINS=['plugins.sitemap', 'plugins.gzip_cache']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


THEME = 'pelican-theme-greyshade'


#

# Subtitle
SITE_SUBTITLE = "The Subtitle"

# All pages are ine the menu by default.
# comment the following line to use the default menu
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
	('About', 'pages/about-this-website'),
	('Nginx', 'pages/nginx'),
	('Pelicanconf', 'pages/pelicanconf'),
    ('Archives', 'blog/archives'),
    ('Authors', 'blog/authors'),
    ('Tags', 'blog/tags'))


# GRAVATAR
import hashlib
m = hashlib.md5()
m.update('me@example.com'.encode('utf-8'))
EMAIL_MD5 = m.hexdigest()
# uncomment the following line to use a custom size
# GRAVATAR_SIZE = 150


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
PINBOARD_USER = "hipster"
DOUBAN_USER = "nickname"
SUBSCRIBE_FEED = True

#


# uncomment the following line to use a Google Analytics
# GOOGLE_ANALYTICS = 1234
