# Generated by Django 4.2.1 on 2023-10-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murino', '0007_occupant_avatar_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='owner',
            field=models.ManyToManyField(related_name='hobbies', to='murino.occupant'),
        ),
    ]