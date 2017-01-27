#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import re
from cia_parser import ciap

params = {}
for param in sys.argv[1:]:
    matches = re.findall(r"-(\w+[^=])=[\'\"]*(.*[^\'\"])", param)
    if len(matches) > 0:
        matches = matches[0]
    else:
        continue
    params[matches[0]] = matches[1]

if params.get('folder') == None:
    params['folder'] = "data"
parser = ciap(params['folder'])

if params.get('year') == None:
    params['year'] = "0"
parser.ParseYear(params['year'])