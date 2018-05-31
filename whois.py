#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:05:45 2018

@author: slytherin
"""

import os

def get_whois(url):
    command="whois "+url
    process=os.popen(command)
    results=str(process.read())
    return results

