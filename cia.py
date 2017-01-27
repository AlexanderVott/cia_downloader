#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import re
from cia_parser import ciap


def printHelp():
    print("Параметры запуска скрипта " + os.path.basename(__file__) + ":\n"
            "-publist= - параметр вывода списка дат публикаций;\n"
            "-pubyear= - параметр сохранения файлов за конкретный год публикации;\n"
            "-folder= - опциональный параметр, указывающий директорию, в которую необходимо сохранять данные;\n"
            "-h, -help= - вызов справки."
            "Например: python " + os.path.basename(__file__) + " -year=1937 -folder='/home/user/data_cia/'\n"
            "Ещё пример: python " + os.path.basename(__file__) + " -year=1937\n"
            "В этом случае данные будут сохраняться в директории \"" + os.path.join(os.getcwd(), "data") + "\", т.е. текущей вашей директории.")

if len(sys.argv) == 1:
    printHelp()
    exit()
if sys.argv[1] in ["-help", "-h", "/h"]:
    printHelp()

params = {}
for param in sys.argv[1:]:
    matches = re.findall(r"-(\w+[^=])=*[\'\"]*(.*[^\'\"])*", param)
    if len(matches) > 0:
        matches = matches[0]
    else:
        continue
    if len(matches) > 1:
        params[matches[0]] = matches[1]
    else:
        params[matches[0]] = ""

if params.get("folder") == None:
    params["folder"] = "data"
parser = ciap(params["folder"], params.get("logfile"))

if params.get("publist") != None:
    parser.ParseYearsList()
else:
    if params.get("pubyear") == None:
        params["pubyear"] = "0"
    parser.ParsePublicatonYear(params["pubyear"])