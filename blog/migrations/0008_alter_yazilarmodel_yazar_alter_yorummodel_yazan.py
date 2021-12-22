# Generated by Django 4.0 on 2021-12-22 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('blog', '0007_iletisimmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazilarmodel',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazilar', to='account.customusermodel'),
        ),
        migrations.AlterField(
            model_name='yorummodel',
            name='yazan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to='account.customusermodel'),
        ),
    ]
