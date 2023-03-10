# space_tg
 
Программа позволяет скачивать фотографии космоса от NASA и SpaceX, а также выкладывать их в Telegram канале.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Также необходим файл `.env`, заполненный следующим образом:

```
NASA_TOKEN=''
TG_TOKEN=''
TG_CHANNEL_ID=''
```

`NASA_TOKEN` - токен API от NASA, получить его можно [здесь](https://api.nasa.gov/).

`TG_TOKEN` - токен API от бота Telegram, вот [инструкция](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) по получению.

`TG_CHANNEL_ID` - id вашего Telegram канала, например `@space_pictures_bot`.

### fetch_spacex_images.py

Скачивает фотографии с последнего запуска SpaceX. Для запуска введите в командную строку:

```console
python fetch_spacex_images.py --launch_id {your_id}
```

По умолчанию скачивает фотографии с последнего запуска, если такие имеются. 

Для скачивания фотографий конкретного запуска, воспользуйтесь опцией `--launch_id` и введите id нужного вам запуска.

### get_epic_earth_pics.py

Скрипт скачивает фотографии Земли с разных ракурсов. Для запуска введите в командную строку:

```console
python get_epic_earth_pics.py
```

### get_space_pictures_of_the_day.py

Скачивает случайные фотографии из ежедневной подборки фотографий космоса от NASA.

```console
python get_space_pictures_of_the_day.py --images_count {x}
```

По умолчанию скачивает 30 фотографий. 

Для скачивания конкретного количества фотографий воспользуйтесь опцией `--images_count` и введите необходимое число.

### tg_publication_script.py 

Скрипт для публикации скачанных фотографий в Telegram канал. 

```console
python tg_publication_script.py  --publication_delay {x}
```

По умолчанию скрипт публикует одну случайную фотографию каждые 4 часа. 

Если хотите изменить задержку постов, воспользуйтесь `--publication_delay` и введите нужное количество часов.

### scripts.py

Вспомогательные скрипты для скачивания картинок.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
