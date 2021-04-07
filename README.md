# NoJpeg_gan

![](https://zigorewslike.github.io/github_rep/nojpeg/example2.png)
NoJpeg_gan - это проект, который убирает сжатие с фотографии с помощью обученной глубокой нейронной сети. Нейронная сеть принимает изображения разрешения 512х512 пикселей.


Пример до обработки и после:
![](https://zigorewslike.github.io/github_rep/nojpeg/example1.png)

# Запуск

```bash
pip install -r requirements.txt
```

> Tensorflow version = 2.4 GPU, т.е. [должна быть cuda](https://www.tensorflow.org/install/gpu#software_requirements)

## Тест 

```bash
-i "data/example.jpg" -o kek.jpg
```

## Трэин 

```bash
-d "Big_dir512/" -c "chachpoint" -e 60 -l 100 -b 400 -r False
```