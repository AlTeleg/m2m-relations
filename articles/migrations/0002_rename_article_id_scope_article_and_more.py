# Generated by Django 4.1 on 2022-08-25 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='article_id',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='scope',
            old_name='tag_id',
            new_name='tag',
        ),
    ]