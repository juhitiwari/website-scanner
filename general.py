#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 22:03:49 2018

@author: slytherin
"""
import os
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    