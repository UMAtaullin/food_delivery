Вы столкнулись с двумя проблемами: предупреждением о том, что вы используете сервер разработки, и отсутствием файла `index.html`. Рассмотрим каждую из них.

## Предупреждение о сервере разработки

Это предупреждение указывает на то, что встроенный сервер Flask предназначен только для разработки и не подходит для производственной среды. Для развертывания приложения в продакшн-режиме рекомендуется использовать WSGI-сервер, такой как **Gunicorn**, **uWSGI** или **Waitress**. Вот пример, как запустить ваше приложение с использованием Gunicorn:

1. Установите Gunicorn:
   ```bash
   pip install gunicorn
   ```

2. Запустите приложение с помощью Gunicorn:
   ```bash
   gunicorn -w 4 page:app
   ```
   Здесь `-w 4` указывает количество рабочих процессов, а `page:app` — это путь к вашему приложению (где `page` — имя файла без `.py`, а `app` — имя экземпляра Flask).

## Проблема с файлом `index.html`

Если Flask не может найти ваш файл `index.html`, это может быть связано с тем, что он должен находиться в специальной папке. Flask ищет шаблоны в директории `templates`, которая должна находиться в той же директории, что и ваш файл `page.py`. Убедитесь, что структура вашего проекта выглядит следующим образом:

```
/ваш_проект
│
├── page.py
└── templates
    └── index.html
```

Если папка `templates` отсутствует или файл `index.html` находится не там, создайте папку `templates` и переместите файл `index.html` в нее.

После выполнения этих шагов ваше приложение должно работать корректно без предупреждений о сервере разработки и находить нужный шаблон.

Citations:
[1] https://discuss.python.org/t/flask-app-deployment/53060
[2] https://stackoverflow.com/questions/51025893/flask-at-first-run-do-not-use-the-development-server-in-a-production-environmen/54381386
[3] https://www.reddit.com/r/flask/comments/10b4kss/flask_server_not_suitable_for_deployment/
[4] https://gist.github.com/jerblack/735b9953ba1ab6234abb43174210d356
[5] https://flask.palletsprojects.com/en/stable/server/
[6] https://community.plotly.com/t/message-warning-this-is-a-development-server-do-not-use-it-in-a-production-deployment/56391
[7] https://flask.palletsprojects.com/en/stable/tutorial/deploy/
[8] https://qna.habr.com/q/1336406