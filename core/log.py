# -*- coding: utf-8 -*-
import os
import time

__author__ = 'AlexanderVott'

# Класс вывода сообщений в лог-файл и консоль
class Log:
    filename = ""
    file = None

    # Инициализация экземпляра класса.
    def __init__(self, filename):
        Log.init(filename)

    # Инициализация статичного класса.
    @staticmethod
    def init(filename):
        import codecs
        if len(filename) == 0 and os.path.exists(filename):
            return
        Log.filename = filename
        Log.file = codecs.open(filename, "w", "utf-8")
        Log.file.write("<log>\n")
        Log.file.flush()

    # Правильное закрытие лог-файла.
    @staticmethod
    def close():
        Log.file.write("</log>")
        Log.file.flush()
        Log.file.close()

    # Базовый метод вывода сообщения.
    # Параметры: тип сообщения, текст сообщения и параметр вывода в консоль
    @staticmethod
    def msg(type, msg, console = True):
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

    # Вывод информационного сообщения.
    # Параметры: текст сообщения, параметр вывода в консоль.
    @staticmethod
    def i(msg, console = True):
        Log.msg("i", msg, console)

    # Вывод предостерегающего сообщения.
    # Параметры: текст сообщения, параметр вывода в консоль.
    @staticmethod
    def w(msg, console = True):
        Log.msg("w", msg, console)

    # Вывод сообщения об ошибке.
    # Параметры: текст сообщения, параметр вывода в консоль.
    @staticmethod
    def e(msg, console = True):
        Log.msg("e", msg, console)

    # Вывод сообщения отладки.
    # Параметры: текст сообщения, параметр вывода в консоль.
    @staticmethod
    def d(msg, console = True):
        Log.msg("d", msg, console)