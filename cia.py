#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import re
from core.log import Log
from cia_parser import ciap


def printHelp():
    print("Параметры запуска скрипта " + os.path.basename(__file__) + ":\n"
            "-publist - параметр вывода списка дат публикаций;\n"
            "-pubyear= - параметр сохранения файлов за конкретный год публикации;\n"
            "-collections - параметр вывода списка сборников публикаций;\n"
            "-collection= - параметр сохранения файлов конкретной коллекции, принимает Id из списка коллекций;\n"
            "-search= - параметр указывает, по какому поисковому запросу загружать документы;\n"
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

if params.get("folder") is None:
    params["folder"] = "data"
parser = ciap(params["folder"], params.get("logfile"))

methods = {
    "search": parser.SearchDownloader,
    "publist": parser.ParseYearsList,
    "pubyear": parser.ParsePublicatonYear,
    "collections": parser.ParseCollections,
    "collection": parser.ParseCollectionById
}

for key in params.keys():
    try:
        if methods.get(key) is not None:
            if params.get(key) == "":
                methods[key]()
            else:
                methods[key](params.get(key))
    except Exception as e:
        Log.e("Ошибка выполнения, не задано значение параметра: " + str(e))