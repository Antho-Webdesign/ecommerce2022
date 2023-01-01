# Generated by Django 4.1.3 on 2022-12-31 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_contactformmodelmixin_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodelmixin',
            options={'ordering': ('-date_sent', 'full_name', 'email', 'subject', 'message', 'cc_myself'), 'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/default.jpg', null=True, upload_to='products/'),
        ),
    ]