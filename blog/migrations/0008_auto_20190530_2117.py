# Generated by Django 2.2.1 on 2019-05-31 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190530_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(default='', max_length=100),
        ),
    ]