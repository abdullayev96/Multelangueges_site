# Generated by Django 4.2 on 2023-05-01 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_contack_name_en_contack_name_ru_contack_name_uz_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contack',
            new_name='Contact',
        ),
    ]