# Generated by Django 4.2.1 on 2025-01-27 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('murino', '0013_hobby_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='KissTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_kisses', models.IntegerField()),
                ('request_date', models.DateField()),
                ('kiss_transaction_status', models.CharField(choices=[('REQD', 'Requested'), ('APPD', 'Approved'), ('DCLD', 'Declined')], default='DCLD', max_length=4)),
                ('requested_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='murino.occupant')),
            ],
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.DeleteModel(
            name='Toy',
        ),
    ]
