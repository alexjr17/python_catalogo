# Generated by Django 4.0.6 on 2022-07-27 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalogo',
            new_name='Producto',
        ),
    ]