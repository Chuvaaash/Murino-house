# Generated by Django 4.2.1 on 2023-05-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('murino', '0005_alter_occupant_page_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='occupant',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='avatars/'),
        ),
    ]
