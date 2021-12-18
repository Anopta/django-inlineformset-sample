from django.db import models

class AppPost(models.Model):
    title = models.CharField('説明書名', max_length=255)

    def __str__(self):
        return  self.title

class AppItem(models.Model):
    item = models.CharField('質問項目追加', max_length=255)
    post = models.ForeignKey(AppPost, verbose_name='紐づく投稿', blank=True, null=True, on_delete=models.CASCADE)
