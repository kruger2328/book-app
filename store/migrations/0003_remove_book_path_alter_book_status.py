# Generated by Django 4.0.4 on 2022-05-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_book_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='path',
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.TextField(),
        ),
    ]
