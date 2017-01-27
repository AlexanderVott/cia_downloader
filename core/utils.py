# -*- coding: utf-8 -*-
import os
import requests
from core.log import Log
import json

class Utils:

    @staticmethod
    def ValidateFileName(filename):
        for char in r"[]/\;,><&*:%=+@!#^()|?^":
            filename = filename.replace(char, "")
        return filename


    @staticmethod
    def DownloadFile(url, folder):
        try:
            filename = os.path.join(folder, url.split('/')[-1])
            r = requests.get(url, stream=True)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            return True
        except Exception as e:
            try:
                Log.e("Ошибка скачивания файла {0} ({1}): {2}".format(url, folder, e))
            except:
                pass
            return False

    @staticmethod
    def ToJson(obj, filename):
        try:
            with open(filename, "w") as f:
                f.write(json.dumps(obj, indent=4))
                f.close()
            return True
        except Exception as e:
            try:
                Log.e("Ошибка записи объекта в файл {0}: {1}".format(filename, e))
            except:
                pass
            return False