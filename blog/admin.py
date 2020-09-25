# ポストを追加、編集、削除する

from django.contrib import admin
from .models import Post  # Postモデルをimport

admin.site.register(Post)  # PostモデルをAdminページ上で見えるようにする
