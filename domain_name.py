#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 22:20:18 2018

@author: slytherin
"""

from tld import get_tld

def get_domain_name(url):
    domain_name=get_tld(url)
    return domain_name

