#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Local settings for {{ PROJECT_NAME }}.
"""


from {{PROJECT_NAME}}.config.common import *


""" Debugging (default True for local environment) """
DEBUG = True
TEMPLATE_DEBUG = DEBUG


""" Databases - sqlite3 default on dev """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/{{ PROJECT_NAME }}.db',
        'USER': '',
        'PASSWORD': '',
    }
}


""" Admins """
ADMINS = (('Name', 'email@email.com'),)
MANAGERS = ADMINS


""" Cacheing (default is dummy, see django docs) """
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
