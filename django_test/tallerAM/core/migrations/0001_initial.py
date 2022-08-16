# Generated by Django 4.1 on 2022-08-16 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='taller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='core')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fechamodificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
