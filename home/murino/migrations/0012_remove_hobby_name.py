# Generated by Django 4.2.1 on 2023-10-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('murino', '0011_alter_hobby_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobby',
            name='name',
        ),
    ]
