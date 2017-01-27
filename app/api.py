# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 12:59:36 2017

@author: manish
"""

from app import api
from models import Comment
api.create_api(Comment,methods=['GET','POST'])
