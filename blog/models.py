from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    # プロパティ定義
    '''
    models.CharField – 文字数が制限されたテキストを定義するフィールド
    models.TextField – これは制限無しの長いテキスト用フィールド
    models.DateTimeField – 日付と時間のフィールド
    models.ForeignKey – 他のモデルへのリンク
    '''
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title  # ポストのタイトルのテキスト（string）を返す
