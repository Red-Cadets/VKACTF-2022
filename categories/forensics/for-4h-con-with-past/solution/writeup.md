# Connection with the past

| Cобытие       | Название       | Категория | Сложность |
|:-------------:|:-------------: |:---------:|:---------:|
| VKAСTF 2022 | Connection with the past| Forensics | Hard |

## Описание

>Автор [Pashkevich]
>
>Разгребал свой сервер и нашел архив с системой. Она запаролена. Интересно узнать, есть ли там что-то полезное.

Пароль от архива: PwECsSsUmNZ5JM9KwM92GzUGCHsES

[Yandex](https://disk.yandex.com/d/kKKK-6JVQyg-vg)
[Google]()

# Решение

Разблокировать поддержку VMWare операционных систем MacOS [чудо утилитой](https://github.com/paolo-projects/unlocker/releases/tag/3.0.4). Для сброса пароля необходимо использовать сторонний загрузчик, имеющий возможность загружать систему с определенными параметрами (например этот: [Clover](https://github.com/CloverHackyColor/CloverBootloader/releases)). Выполняем загрузку с параметрами `npci=0x2000 keepsyms=1 -s`. Далее необходимо выполнить сам сброс пароля (мануал [тут](https://btip.ru/izmenenie-parolya-administratora-v-odnopolzovatelskom-rezhime-mac-os-x/)). После входа в систему обнаружится, что не работает сеть. Однако необходимо изучить историю браузера где будет ссылка на файлообменник и *.kext* файл – собственно драйвер сети. 
Открываем содержимое пакета, по пути `/IONetworkingFamily.kext/Contents/PlugIns/Flag.app` внутри *Flag.app* лежит файл окружения Automator'a. В нём – флаг.

Необязательно:
Для инициализации сети драйвер перемещаем по пути */System/Library/Extensions/* и индексируем папку утилитой *Kext Utility* (лежит в папке с приложениями в каталоге утилит). 

### Флаг
```
vka{h3ll0_fr0m_7h3_p457_w17h_l0v3}
```
