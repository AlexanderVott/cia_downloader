from datetime import datetime
from dateutil.relativedelta import relativedelta
import lxml.html as html
import urllib.request as request
import re

class document:
    def __init__(self, name, link, description):
        self.name = name
        self.link = link
        self.description = description
        self.info = {}

class ciap:
    _link_parse = "https://www.cia.gov/library/readingroom/search/site/?{0}f[0]=dm_field_release_date%3A[{1}T00%3A00%3A00Z%20TO%20{2}T00%3A00%3A00Z]"

    def __init__(self):
        pass

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
            # TODO: заменить на запись в log-файл
            print(str(e))
            return ""

    def parseLast(self, url_main):
        """
        :param url_main: ссылка на главную страницу обработки
        :return:
        """
        # TODO: в дальнейшем необходимо главной ссылкой считать ссылку на сам архив, а не на его отдельный раздел
        content = self.readContent(url_main)
        page_first = html.document_fromstring(content)
        href = page_first.xpath("//li[@class='pager-last last']//a")[0].attrib['href']
        last = re.search(r"page=(\d+)&", href)
        return int(last.group(1))

    def parseListPage(self, url):
        content = self.readContent(url)
        page_list = html.document_fromstring(content)
        list = page_list.xpath("//ol[@class='search-results apachesolr_search-results']//li")
        documents = []
        for item in list:
            hthree, div = item.getchildren()
            hthree = hthree.getchildren()[0]
            link = hthree.attrib['href']
            name = hthree.text
            description = div.getchildren()[0].text
            print(name + ": " + link)
            print(description)
            doc = document(name, link, description)
            doc.info = self.parseDocPage(link)
            documents.append(doc)

        return documents

    def parseDocPage(self, url):
        content = self.readContent(url)
        page_doc = html.document_fromstring(content)
        infoBlock = page_doc.xpath("//div[@class='content clearfix']")[0].getchildren()
        dict = {}
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
        return dict

    def Parse(self, year):
        """

        :param date: дата которую надо разобрать из архива
        :return:
        """

        date_format = "{0}-01-01"
        date_0 = datetime.strptime(date_format.format(year), "%Y-01-01").date()
        date_1 = date_0 + relativedelta(years=1)
        maxPages = self.parseLast(self._link_parse.format("", date_0, date_1))
        for i in range(1, maxPages + 1):
            self.parseListPage(self._link_parse.format("page=" + str(i) + "&", date_0, date_1))
