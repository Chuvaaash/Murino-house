# Generated by Django 4.2.1 on 2025-01-28 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murino', '0014_kisstransaction_delete_items_delete_toy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisstransaction',
            name='requested_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='murino.occupant'),
        ),
    ]
