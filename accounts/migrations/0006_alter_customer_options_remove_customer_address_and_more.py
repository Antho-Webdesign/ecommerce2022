# Generated by Django 4.1.3 on 2022-11-26 01:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customer_options_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zip_code',
        ),
    ]
