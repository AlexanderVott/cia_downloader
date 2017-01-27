#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from dateutil.relativedelta import relativedelta
import lxml.html as html
import urllib.request as request
import re
from core.log import Log
import os.path as path
import os
import json
import requests
import time

class document:
    def __init__(self, name, link, description, file):
        self.name = name
        self.link = link
        self.description = description
        self.file = file
        self.info = {}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class ciap:
    _link_parse = "https://www.cia.gov/library/readingroom/search/site/?{0}f[0]=dm_field_release_date%3A[{1}T00%3A00%3A00Z%20TO%20{2}T00%3A00%3A00Z]"
    _folder = ""
    _items = {}
    _errors = False

    def __init__(self, folder):
        Log.init("log.xml")
        Log.i("Парсер инициализирован.")
        self._folder = folder
        if path.exists(self._folder) == False:
            os.mkdir(self._folder)
        Log.i("Данных сохраняются в {0}".format(folder))

        pass

    def validate(self, filename):
        for c in r'[]/\;,><&*:%=+@!#^()|?^':
            filename = filename.replace(c,'')
        return filename

    def readContent(self, url):
        """
            Метод читает содержимое страницы по ссылке.
        :rtype: str
        """
        try:
            req = request.Request(url)
            opener = request.build_opener()
            res = opener.open(req)
            return res.read()
        except Exception as e:
            self._errors = True
            Log.e("Ошибка получения содержимого страницы ({0}): {1}".format(url, e))
            return ""

    def downloadFile(self, url, folder):
        try:
            filename = path.join(folder, url.split('/')[-1])
            r = requests.get(url, stream=True)
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        except Exception as e:
            self._errors = True
            Log.e("Ошибка скачивания файла {0} ({1}): {2}".format(url, folder, e))

    def parseLast(self, url_main):
        """
        :param url_main: ссылка на главную страницу обработки
        :return:
        """
        # TODO: в дальнейшем необходимо главной ссылкой считать ссылку на сам архив, а не на его отдельный раздел
        content = self.readContent(url_main)
        if len(content) == 0:
            return 0
        page_first = html.document_fromstring(content)
        href = page_first.xpath("//li[@class='pager-last last']//a")[0].attrib['href']
        last = re.search(r"page=(\d+)&", href)
        return int(last.group(1))

    def parseListPage(self, url, folder):
        content = self.readContent(url)
        if len(content) == 0:
            return []
        page_list = html.document_fromstring(content)
        list = page_list.xpath("//ol[@class='search-results apachesolr_search-results']//li")
        Log.i("{0} элемента(ов)...".format(len(list)))
        documents = []
        for item in list:
            try:
                hthree, div = item.getchildren()
                hthree = hthree.getchildren()[0]

                link = hthree.attrib['href']
                name = hthree.text
                description = div.getchildren()[0].text

                doc = document(name, link, description, self.validate(name) + ".json")
                Log.i("Обрабатывается документ {0}: {1}".format(name, link))
                doc.info = self.parseDocPage(link, folder)

                self._items[name] = "{0}\n{1}\n{2}".format(description, link, doc.file)
                self.saveDocInfo(path.join(folder, doc.file), doc)

                documents.append(doc)
            except Exception as e:
                self._errors = True
                Log.e("Неудалось обработать страницу: {0}".format(e))

        return documents

    def parseDocPage(self, url, folder):
        content = self.readContent(url)
        if len(content) == 0:
            return {}
        page_doc = html.document_fromstring(content)
        infoBlock = page_doc.xpath("//div[@class='content clearfix']")[0].getchildren()
        dict = {}
        try:
            for item in infoBlock:
                key, value = item.getchildren()
                key = re.search(r"(\D+):", key.text).group(1)
                values = []
                for v in item.getchildren()[1].getchildren():
                    if len(v.getchildren()) == 0:
                        values.append(v.text)
                    else:
                        child = v.getchildren()[0]
                        if child.attrib.get('href'):
                            values.append(child.attrib['href'])
                        values.append(child.text)
                dict[key] = values
        except Exception as e:
            self._errors = True
            Log.e("Неудалось обработать информационный блок: {0}".format(e))
        attachments_doc = page_doc.xpath("//table/tbody/tr")
        attachments = []
        try:
            for attach in attachments_doc:
                attach_childs = attach.getchildren()
                for i in range(len(attach_childs)):
                    if attach_childs[i].text != None:
                        Log.i("Скачивается файл {0}: {1}".format(attach_childs[0][0][1].text,
                                                                 attach_childs[0][0][1].attrib['href']))
                        attachments.append(attach_childs[0][0][1].text)
                        self.downloadFile(attach_childs[0][0][1].attrib['href'], path.join(folder, "files"))
        except Exception as e:
            self._errors = True
            Log.e("Неудалось обработать блок вложений: {0}".format(e))
        dict['attachments'] = attachments
        return dict

    def saveDocInfo(self, file, obj):
        try:
            with open(path.join(file), "w") as f:
                f.write(obj.toJSON())
                f.close()
        except Exception as e:
            self._errors = True
            Log.e("Ошибка записи файла {0}: {1}".format(file, e))

    def saveItems(self, folder):
        try:
            with open(path.join(folder, "items.json"), "w") as f:
                f.write(json.dumps(self._items, indent=4))
                f.close()
        except Exception as e:
            self._errors = True
            Log.e("Ошибка записи элементов: {0}".format(e))

    def ParseYear(self, year):
        """

        :param date: дата которую надо разобрать из архива
        :return:
        """

        workFolder = path.join(self._folder, year)
        filesFolder = path.join(workFolder, "files")
        if path.exists(filesFolder) == False:
            os.makedirs(filesFolder)

        start_time = time.time()

        Log.i("Скачивается {0} год".format(year))
        date_format = "{0}-01-01"
        date_0 = datetime.strptime(date_format.format(year), "%Y-01-01").date()
        date_1 = date_0 + relativedelta(years=1)
        maxPages = self.parseLast(self._link_parse.format("", date_0, date_1))
        Log.i("Количество страниц: {0} ...".format(maxPages))

        for i in range(1, maxPages + 1):
            Log.i("********************************************************")
            Log.i("Обрабатывается страница {0}: {1}".format(i, self._link_parse.format("page=" + str(i) + "&", date_0, date_1)))
            self.parseListPage(self._link_parse.format("page=" + str(i) + "&", date_0, date_1), workFolder)

        Log.i("Сохраняем список документов за год...")
        self.saveItems(workFolder)

        end_time = time.time()

        if self._errors:
            Log.w("Скачивание завершено с ошибками!")
        else:
            Log.i("Скачивание завершено.")
        Log.i("Времени затрачено: {:.3f} секунд".format(end_time - start_time))
