# Generated by Django 4.0 on 2021-12-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_appitem_apppost_delete_file_delete_post_appitem_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appitem',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.apppost', verbose_name='紐づく投稿'),
        ),
    ]