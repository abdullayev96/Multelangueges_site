# Generated by Django 4.2 on 2023-05-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_options_remove_contact_number_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=2, upload_to='images', verbose_name='Rasmlar'),
            preserve_default=False,
        ),
    ]
