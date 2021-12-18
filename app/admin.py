from django.contrib import admin
from .models import *


class FileInline(admin.StackedInline):
    model = AppItem
    extra = 0


class AppPostAdmin(admin.ModelAdmin):
    inlines = [FileInline]


admin.site.register(AppPost, AppPostAdmin)
admin.site.register(AppItem)  # 一応、ファイル単体の管理画面も作っておく
