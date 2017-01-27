# cia_downloader
Скачивает рассекреченные документы вместе с описанием.

###Требования:

Для корректной работы требуется ```Python >= 3.5.2```

Установка зависимостей:
```commandline
pip install -r req.txt
```

###Вывод списка дат публикаций:

```commandline
python cia.py -publist
```

###Запуск и использование скачивания по годам публикаций:

```commandline
python cia.py -folder="/home/user/cia_docs/" -pubyear=1937
```

Учитывается год публикации документа (Release date).
Результат будет храниться в директории ```/home/user/cia_docs/1937```
Параметр ```folder``` является опциональным, при его отсутствии данные будут сохраняться в каталог ```data/``` внутри директории утилиты.