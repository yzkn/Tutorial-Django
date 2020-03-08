# Tutorial-Django

---

## Python をインストール

[Download Python](https://www.python.org/downloads/) から最新版の Python インストーラー( [Feb. 24, 2020 時点](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64-webinstall.exe) )をダウンロードして実行

## (Option) DB をインストール

PostgreSQL または MariaDB、MySQL、Oracle のような "large" database engine を利用する場合はインストールしておく

## Django をインストール

```ps
$ cd C:\Users\y\Documents\GitHub\Tutorial-Django
$ py -m venv djangoenv
$ .\djangoenv\Scripts\activate
$ py -m pip install Django
Collecting Django
  Downloading Django-3.0.4-py3-none-any.whl (7.5 MB)
     |████████████████████████████████| 7.5 MB 2.2 MB/s
Collecting asgiref~=3.2
  Downloading asgiref-3.2.3-py2.py3-none-any.whl (18 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.3.1-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 2.7 MB/s
Collecting pytz
  Downloading pytz-2019.3-py2.py3-none-any.whl (509 kB)
     |████████████████████████████████| 509 kB 2.2 MB/s
Installing collected packages: asgiref, sqlparse, pytz, Django
Successfully installed Django-3.0.4 asgiref-3.2.3 pytz-2019.3 sqlparse-0.3.1
$ py
>>> import django
>>> print(django.get_version())
3.0.4
```

## プロジェクトを作成

```ps
$ django-admin startproject myproj
$ cd myproj
```

### 動作確認

```ps
$ py manage.py runserver
```

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)にアクセスして、 `The install worked successfully! Congratulations!` と表示されていることを確認する

## アプリケーションを作成

```ps
$ py manage.py startapp myapp
```

### ビューを編集

`myapp/views.py` に以下を追記する

```py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

`myapp/urls.py` を作成して、以下を追記する

```py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

`myproj/urls.py` を以下のように変更する

```py
//from django.urls import path
from django.urls import include, path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
```

### 動作確認

```ps
$ py manage.py runserver
```

[http://127.0.0.1:8000/myapp](http://127.0.0.1:8000/myapp)にアクセスして、 `This is the index view.` と表示されていることを確認する（ [http://127.0.0.1:8000/](http://127.0.0.1:8000/) ではなく [http://127.0.0.1:8000/myapp](http://127.0.0.1:8000/myapp) であることに気を付ける）
