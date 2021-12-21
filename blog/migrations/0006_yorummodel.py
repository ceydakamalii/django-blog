# Generated by Django 4.0 on 2021-12-21 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0005_alter_yazilarmodel_icerik'),
    ]

    operations = [
        migrations.CreateModel(
            name='YorumModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('duzenleme_tarihi', models.DateTimeField(auto_now=True)),
                ('yazan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to='auth.user')),
                ('yazi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='blog.yazilarmodel')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'db_table': 'Yorum',
            },
        ),
    ]