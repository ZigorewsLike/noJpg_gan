# NoJpeg_gan

JPEG или JPG является широко используемым методом сжатия с потерями для цифровых изображений, особенно для тех изображений, полученных с помощью цифровой фотографии. JPEG использует форму сжатия с потерями, основанную на дискретном косинусном преобразовании (DCT).


**NoJpeg_gan** - это проект, который убирает сжатие с JPG фотографии с помощью обученной глубокой нейронной сети. Нейронная сеть принимает изображения разрешения 512х512 пикселей.


Пример до обработки и после:
![example 1](https://zigorewslike.github.io/github_rep/nojpeg/example1.png)

Нейронная сеть обучена на 4 тысячах изображениях природы, птиц, т.е. нейронная  сеть плохо работает на людях и технике.

# Установка

## Tensorflow-gpu

Для установки данного проекта необходим python 3.7 и Tensorflow 2.4.0 (Данная версия необходима для тестирования на обученной модели. При обучении можно использовать версию новее). Tensorflow для обучения использует GPU, т.е. [необходимо настроить среду для работы с Cud'ой и Cdnn](https://www.tensorflow.org/install/gpu#software_requirements).

> Т.к. используется инструмент Cuda для обучения, AMD видеокарты для этих целей не подойдут.

> !! Tf-nightly версия не работает на данной архитектуре и может поломать Cud'у у владельцах видеокарты RTX3080.

Необходимо установить все библиотеки
```bash
pip install -r requirements.txt
```

## DVC

В проекте инициализировал dvc. По возможности можно запросить доступ к данным, либо [изменить удалённый репозиторий](https://dvc.org/doc/command-reference/remote/add)

Dvc не указан в файле requirements, т.к. является не обязательным.
В случае необходимости нужно прописать следующую команду.
```bash
pip install dvc dvc[gdrive]
```
dvc[gdrive] - это расширение dvc для подключения гугл диска. Подробнее для [Windows](https://dvc.org/doc/install/windows#install-with-pip) и [Linux](https://dvc.org/doc/install/linux#install-with-pip) систем.

# Тестирование модели на своих данных

> Нейронная сеть принимает расширение 512х512 пикселей, т.е. изображения больше, чем 512 по сторонам будут уменьшены до 512.

Протестировать обученную модель на своих данных можно с помощью скрипта ``test_val.py`` с параметрами:
- `-i` - Путь к изображению, 
- `-o` - Путь к итоговому изображению,
- `-m` - Путь к модели.

Для ознакомления можно скачать и использовать обученную модель генератора (не является чекпоинтом). 
[Ссылка на модель](https://drive.google.com/file/d/1uOF5fRBB_sAsSJywRlaK0R4n7ZjDYT2S/view?usp=sharing).

Пример запуска:
```bash
test_val.py -i "example.jpg" -o result.jpg  -m model/g512m.h5
```

# Подготовка данных к обучению

Данные для обучения представляют собой изображения 1024х512, где располагаются два изображения. Первое изображение располагается в левом углу и представляет собой входное изображение (input image), а второе изображение является тем, что нейронная сеть должна получить, так называемый ground truth. Первое изображение подвергается сжатию со случайной степенью.

Пример такого изображения:
![exmaple 3](https://zigorewslike.github.io/github_rep/nojpeg/example3.jpg)

Данные располагаются в папке train, test. Для получения такого сета изображений необходимо запустить скрипт ``collect_data.py`` с параметрами запуска:
- `-i` - Путь к папке с изображениями,
- `-o` - Директория, где создаются 3 папки (data, train, test), которые хранят готовые для обучения изображения,
- `-t` - Доля тестовой выборки в датасете [0, 1].

Пример запуска:
```
collect_data.py -i "data/Big_dir512" -o "dataset" -t 0.20
```

# Обучение модели 

Для обучения нужно запустить скрипт ``train.py`` с параметрами:
- `-d` - Путь к директории, содержащая папки `data`, `train`, `test` (Указать путь на директорию, т.е. в конце пути добавить `/`),
- `-c` - Путь к директории, где хранятся "чекпоинты",
- `-e` - Количество эпох,
- `-l` - Значение lambda для расчёта потери генератора,
- `-b` - Размер буфера,
- `-r` - Restore, т.е. загрузить "чекпоинт" перед обучением, который находится в директории (её указывает параметр `-c`).

Пример запуска:
```bash
train.py -d "Big_dir512/" -c "checkpoint_dir" -e 60 -l 100 -b 400 -r False
```
