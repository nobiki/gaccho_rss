#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages

setup(
        name             = 'gaccho_rss',
        version          = '0.0.3',
        description      = 'Gaccho Rss Feed Plugin',
        license          = 'MIT',
        author           = 'nobiki',
        author_email     = 'test@example.com',
        url              = 'https://github.com/nobiki/gaccho_rss.git',
        keywords         = 'gaccho rss',
        packages         = find_packages(),
        install_requires = [
            "feedparser==5.2.1",
            ],
        )

