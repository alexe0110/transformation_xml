# transformation_xml

* Удаляет черточки из XML файла (file.xml в корневой директории)
* Преобразует формат SAP к формату SOPA UI
* Заменяет хедер и футер

### Установка

**Примечание**: Требуемая версия python 3.7 и выше.

```bash
# Клонировать репозиторий
$ git clone https://github.com/alexe0110/transformation_xml.git

# Войти в рабочий каталог
$ cd ~/transformation_xml

# Запустить как указано ниже
```

### Запуск
```bash
python main.py file_name.xml
```
Или без указания названия файла, в таком случае будет использовано стандартное название файла file.xml
```bash
python main.py
```
