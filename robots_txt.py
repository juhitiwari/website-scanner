#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:59:59 2018

@author: slytherin
"""

import urllib.request
import io

def get_robots_txt(url):
    if url.endswith('/'):
        path=url
    else:
        path=url+'/'
    
    req=urllib.request.urlopen(path+"robots.txt",data=None)
    data=io.TextIOWrapper(req,encoding='UTF-8')
    return data.read()

