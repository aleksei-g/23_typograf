# Typograf Service

# Типограф

Данное приложение позволяет подготовить русский текст для публикации в вебе.

В текущей редакции реализованы следующие правила:
* замена кавычек ' и " на « »
* дефисы между словами заменяются на тире
* замена дефисов на короткое тире в номерах телефонов
* замена дефиса на неразрывный дефис между числом и словом
* удаление лишних пробелов и переносов строк
* связывание союзов и любых слов из 1-2 символов с последующими словами
* связывание неразрывным пробелом чисел с последующими словами.

Для запуска приложения необходимо выполнить команду:
```
python server.py
```
, затем перейти по адресу [127.0.0.1:5000](http://127.0.0.1:5000/), 
где можно ввести текст для обработки.

Для корректоной работы необходимо установить следующие модули:
* **flask**

Пакеты устанавливаются командой `pip install -r requirements.txt`.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)