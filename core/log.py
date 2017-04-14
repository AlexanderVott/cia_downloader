# -*- coding: utf-8 -*-
import os
import time

__author__ = 'AlexanderVott'


class Log:
    """
    Класс вывода сообщений в файл-журнала и консоль.
    """

    filename = ""
    file = None

    def __init__(self, filename):
        """
        Инициализация экземпляра класса.
        :param filename: путь до файла в который будет производиться запись сообщений журнала.
        """
        Log.init(filename)

    @staticmethod
    def init(filename):
        """
        Инициализация статичного класса журнала.
        :param filename: путь до файла в который будет производиться запись сообщений журнала.
        :return: 
        """
        import codecs
        if len(filename) == 0 and os.path.exists(filename):
            return
        Log.filename = filename
        Log.file = codecs.open(filename, "w", "utf-8")
        Log.file.write("<log>\n")
        Log.file.flush()

    @staticmethod
    def close():
        """
        Правильное закрытие файла-журнала.
        :return: 
        """
        Log.file.write("</log>")
        Log.file.flush()
        Log.file.close()

    @staticmethod
    def msg(type, msg, console = True):
        """
        Базовый метод вывода сообщений.
        :param type: тип сообщения.
        :param msg: текст сообщения.
        :param console: указывает необходимо ли выводить данные в консоль. По умолчанию true.
        :return: 
        """
        _type = {
            'i': u"Info",
            "w": u"Warning",
            "e": u"Error",
            "d": u"Debug"
        }.get(type)
        timeValue = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
        if Log.file is None:
            Log.init("log.xml")
        if msg is None:
            umsg = "None"
        else:
            '''if isinstance(msg, unicode):
                umsg = msg
            elif isinstance(msg, str):
                umsg = unicode(msg, "utf-8")
            else:'''
            umsg = str(msg)
        Log.file.write(u"    <{0} time=\"{1}\">{2}</{0}>\n".format(_type, timeValue, umsg))
        Log.file.flush()
        if console:
            print(u"[{0}][{1}] {2}".format(type, timeValue, umsg))

    @staticmethod
    def i(msg, console = True):
        """
        Вывод информационного сообщения.
        :param msg: текст сообщения.
        :param console: указывает необходимо ли выводить данные в консоль. По умолчанию true.
        :return: 
        """
        Log.msg("i", msg, console)

    @staticmethod
    def w(msg, console = True):
        """
        Вывод предостерегающего сообщения.
        :param msg: текст сообщения.
        :param console: указывает необходимо ли выводить данные в консоль. По умолчанию true. 
        :return: 
        """
        Log.msg("w", msg, console)

    @staticmethod
    def e(msg, console = True):
        """
        Вывод сообщения об ошибке.
        :param msg: текст сообщения.
        :param console: указывает необходимо ли выводить данные в консоль. По умолчанию true. 
        :return: 
        """
        Log.msg("e", msg, console)

    @staticmethod
    def d(msg, console = True):
        """
        Вывод сообщения отладки.
        :param msg: текст сообщения.
        :param console: указывает необходимо ли выводить данные в консоль. По умолчанию true. 
        :return: 
        """
        Log.msg("d", msg, console)