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

###Параметры запуска:
Параметры запуска скрипта ```cia```:
* ```-publist``` - параметр вывода списка дат публикаций;
* ```-pubyear=``` - параметр сохранения файлов за конкретный год публикации;
* ```-collections``` - параметр вывода списка сборников публикаций;
* ```-collection=``` - параметр сохранения файлов конкретной коллекции, принимает Id из списка коллекций;
* ```-search=``` - параметр указывает, по какому поисковому запросу загружать документы;
* ```-folder=``` - опциональный параметр, указывающий директорию, в которую необходимо сохранять данные;
* ```-h```, ```-help=``` - вызов справки.

###Список годов публикаций:
```
  №. год  (количество документов)
  1. 2014 (1)
  2. 2011 (8)
  3. 2010 (127)
  4. 2009 (267)
  5. 2008 (126)
  6. 2007 (153)
  7. 2006 (122)
  8. 2005 (125)
  9. 2004 (100)
 10. 2003 (104)
 11. 2002 (70)
 12. 2001 (118)
 13. 2000 (716)
 14. 1999 (621)
 15. 1998 (770)
 16. 1997 (220)
 17. 1996 (215)
 18. 1995 (549)
 19. 1994 (727)
 20. 1993 (677)
 21. 1992 (932)
 22. 1991 (1353)
 23. 1990 (2125)
 24. 1989 (2736)
 25. 1988 (10187)
 26. 1987 (10784)
 27. 1986 (18084)
 28. 1985 (22920)
 29. 1984 (19505)
 30. 1983 (43831)
 31. 1982 (20744)
 32. 1981 (13816)
 33. 1980 (11536)
 34. 1979 (9561)
 35. 1978 (14583)
 36. 1977 (11700)
 37. 1976 (20261)
 38. 1975 (15486)
 39. 1974 (19819)
 40. 1973 (12311)
 41. 1972 (20597)
 42. 1971 (13151)
 43. 1970 (16063)
 44. 1969 (13685)
 45. 1968 (14581)
 46. 1967 (55809)
 47. 1966 (20885)
 48. 1965 (23807)
 49. 1964 (24783)
 50. 1963 (25881)
 51. 1962 (18528)
 52. 1961 (16529)
 53. 1960 (17601)
 54. 1959 (26100)
 55. 1958 (23491)
 56. 1957 (21158)
 57. 1956 (23067)
 58. 1955 (26037)
 59. 1954 (33584)
 60. 1953 (35989)
 61. 1952 (31821)
 62. 1951 (27938)
 63. 1950 (24397)
 64. 1949 (17536)
 65. 1948 (11642)
 66. 1947 (10133)
 67. 1946 (4271)
 68. 1945 (1754)
 69. 1944 (1534)
 70. 1943 (500)
 71. 1942 (253)
 72. 1941 (61)
 73. 1940 (2)
 74. 1900 (31)
```

###Список сборников:
```
  №    Id    Название (количество документов)
  1.      45 A Life in Intelligence - The Richard Helms Collection (834)
  2.       1 A-12 OXCART Reconnaissance Aircraft Documentation (351)
  3.      15 Air America: Upholding the Airmen's Bond (92)
  4.  724287 An Underwater Ice Station Zebra: Recovering a Secret Spy Satellite Capsule from 16,400 feet Below the Pacific Ocean (37)
  5.  724281 Atomic Spies: Ethel and Julius Rosenberg (102)
  6.      44 Baptism By Fire: CIA Analysis of the Korean War Overview   (1355)
  7.    4186 Bay of Pigs Release (8)
  8. 1834879 Berlin Tunnel (1)
  9. 1817859 Bosnia, Intelligence, and the Clinton Presidency (341)
 10. 1700321 CIA Analysis of the Warsaw Pact Forces (1078)
 11.    4187 CIA Declassifies Oldest Documents in U.S. Government Collection (6)
 12. 1820543 CIA's Clandestine Services: Histories of Civil Air Transport (4)
 13. 1834880 Consolidated Translations (33657)
 14.      50 Creating Global Intelligence (840)
 15.  190759 CREST: 25-Year Program Archive (2585)
 16. 1822445 Declassified Articles from Studies in Intelligence: The IC’s Journal for the Intelligence Professional (242)
 17. 1822840 DECLASSIFIED DOCUMENTS RELATED TO 9/11 ATTACKS (6)
 18. 1822135 Doctor Zhivago (98)
 19. 1829767 Documents Related to the Former Detention and Interrogation Program (50)
 20.   89801 FOIA Collection (19006)
 21.  724285 Francis Gary Powers: U-2 Spy Pilot Shot Down by the Soviets (71)
 22. 1820853 From Typist to Trailblazer: The Evolving View of Women in the CIA's Workforce (117)
 23. 1834881 General CIA Records (768793)
 24. 1834882 Ground Photo Caption Cards (15173)
 25.       3 Guatemala (5120)
 26.  724279 Human Rights in Latin America (624)
 27. 1700319 Intelligence, Policy, and Politics: The DCI, the White House, and Congress (1358)
 28. 1829750 John McCone as Director of Central Intelligence, 1961-1965 (2)
 29. 1834883 JPRS (2554)
 30. 1834884 Library of Congress (7895)
 31.  724283 Lt. Col. Oleg Penkovsky: Western Spy in Soviet GRU (179)
 32.      11 National Intelligence Council (NIC) Collection (1151)
 33. 1705143 Nazi War Crimes Disclosure Act (56252)
 34. 1834885 NGA Records (Formerly NIMA) (63731)
 35. 1834886 NIS (442)
 36. 1834887 OSS Collection (336)
 37.  724275 POW MIA (802)
 38.      47 Preparing for Martial Law: Through the Eyes of Colonel Ryszard Kuklinski (86)
 39. 1821105 President Carter and the Role of Intelligence in the Camp David Accords (258)
 40. 1699355 President Nixon and the Role of Intelligence in the 1973 Arab-Israeli War (419)
 41. 1827265 President's Daily Brief 1961-1969 (2484)
 42. 1829819 President's Daily Brief 1969-1977 (2527)
 43.      17 Reagan Collection (206)
 44. 1834888 Scientific Abstracts (33072)
 45. 1834889 Secret Writing (6)
 46.      46 Soviet and Warsaw Pact Military Journals (804)
 47. 1088023 Soviet and Warsaw Pact Military Journals (Latest) (88)
 48. 1834890 STARGATE (12473)
 49. 1818029 Stories of Sacrifice & Dedication (895)
 50.      19 Strategic Warning and the Role of Intelligence: Lessons Learned From The 1968 Soviet Invasion of Czechoslovakia (542)
 51. 1822440 The Berlin Wall Collection: A City Torn Apart: Building of the Berlin Wall (378)
 52.      14 The CAESAR, POLO, and ESAU Papers (149)
 53.      13 The China Collection (71)
 54.  724273 The Family Jewels   (1)
 55.      49 The Original Wizards of Langley (59)
 56.      52 The Princeton Collection (907)
 57.      12 The Vietnam Collection (174)
 58.       2 UFOs: Fact or Fiction? (243)
 59.      48 Vietnam Histories (6)
 60.      43 Wartime Statutes - Instruments of Soviet Control (22)
 61.      18 What was the Missile Gap? (189)
```