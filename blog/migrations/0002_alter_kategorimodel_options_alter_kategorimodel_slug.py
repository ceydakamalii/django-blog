# Generated by Django 4.0 on 2021-12-21 20:22

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorimodel',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterField(
            model_name='kategorimodel',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='isim', unique=True),
        ),
    ]
