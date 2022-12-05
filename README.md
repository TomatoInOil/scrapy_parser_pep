# Проект парсинга peps.python.org
## Оглавление
1. [Описание](https://github.com/TomatoInOil/scrapy_parser_pep#описание)
2. [Используемые технологии](https://github.com/TomatoInOil/scrapy_parser_pep#используемые-технологии)
3. [Как развернуть проект?](https://github.com/TomatoInOil/scrapy_parser_pep#как-развернуть-проект)
4. [Автор](https://github.com/TomatoInOil/scrapy_parser_pep#автор)
## Описание
Асинхронный парсер `peps.python.org`, который собирает информацию о документах PEP со страницы их карточки (номер, название, статус), приэтом создаётся сводная таблица по статусам. 
## Используемые технологии
- `Python`
- `Scrapy`
## Как развернуть проект?
Склонировать репозиторий 
```BASH
git clone https://github.com/TomatoInOil/scrapy_parser_pep.git
```
Перейти в корневую папку проекта
```BASH
cd scrapy_parser_pep/
```
Создать виртуальное окружение
```BASH
python -m venv venv
```
Активировать виртуальное окружение
```BASH
source venv/Scripts/activate
```
Установить зависимости
```BASH
pip install -r requirements.txt
```
Запустить парсер
```BASH
scrapy crawl pep
```
## Автор
Проект выполнен в рамках учебы в Яндекс.Практикум [Даниилом Паутовым](https://github.com/TomatoInOil) =^..^=______/
