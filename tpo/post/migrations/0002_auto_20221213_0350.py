# Generated by Django 2.2.13 on 2022-12-13 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicationsDate',
            field=models.DateField(verbose_name='Fecha de publicacion'),
        ),
    ]
