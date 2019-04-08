from django.contrib import admin
from .models import *


class FileInline(admin.StackedInline):
    model = File
    extra = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [FileInline]


admin.site.register(Post, PostAdmin)
admin.site.register(File)  # 一応、ファイル単体の管理画面も作っておく
