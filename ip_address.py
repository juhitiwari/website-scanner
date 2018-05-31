#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 23:07:24 2018

@author: slytherin
"""

import os

def get_ip_address(url):
    command="host "+url
    process=os.popen(command)
    results=str(process.read())
    marker=results.find('has address')+12
    return results[marker:].splitlines()[0]

