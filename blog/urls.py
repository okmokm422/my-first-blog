# path 関数と、blog アプリの全ての ビューをインポート
from django.urls import path
from . import views

# post_list という名前の ビュー をルートURLに割り当て
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
