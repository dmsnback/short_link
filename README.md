[](#Начало)

# YaCut



- [Описание](#Описание)
- [Технологии](#Технологии)
- [Запуск](#Запуск)
- [Автор](#Автор)

### Описание

Проект __YaCut__ — это сервис укорачивания ссылок. 

Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Доступны web и REST API интерфейсы


#### Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

#### API для проекта

- ```/api/id/``` — POST-запрос на создание новой короткой ссылки;
- ```/api/id/<short_id>/``` — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Примеры запросов к API, варианты ответов и ошибок приведены в спецификации ```openapi.yml```
#


### Технологии

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)
#

<a name="Запуск"></a>
### Запуск

- __Склонируйте репозиторий__

```python
git clone git@github.com:dmsnback/yacut.git
```
- __Перейдите в директорию с проектом__ 
```python
cd yacut
```

- __Установите и активируйте виртуальное окружение__
```python
python3 -m venv venv
```
Для ```Windows```
```python
source venv/Scripts/activate
```
Для ```Mac/Linux```
```python
source venv/bin/activate
```
- __Установите зависимости из файла__ ```requirements.txt```

```python
python3 -m pip install --upgrade pip
```
```python
pip install -r requirements.txt
```

- __В корневой директории создайте файл__ ```.env```
```python
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SUPER_SECRET_KEY
```

- __Выполните миграции__
```python
flask db migrate
```
```python
flask db upgrade
```
- __Запустите приложение__
```python
flask run
```

#
<a name="Автор"></a>

### Автор

- [Титенков Дмитрий](https://github.com/dmsnback)

[Вернуться в начало](#Начало)
