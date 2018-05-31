#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 10:54:30 2018

@author: slytherin
"""

import os

def get_nmap(options,ip):
    command="nmap "+options+" "+ip
    process=os.popen(command)
    results=str(process.read())
    return  results

