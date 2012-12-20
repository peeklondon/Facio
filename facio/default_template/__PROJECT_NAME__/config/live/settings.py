#!/usr/bin/env python
# encoding: utf-8
"""
settings.py

Live environment settings for {{ PROJECT_NAME }}.
"""


from {{PROJECT_NAME}}.config.common import *


""" Debugging (default True for local environment) """
DEBUG = True
TEMPLATE_DEBUG = DEBUG


""" Databases - mysql default on live/production """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
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
