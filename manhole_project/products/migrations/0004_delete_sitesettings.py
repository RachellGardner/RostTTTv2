# Generated by Django 5.2.4 on 2025-07-13 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_sitesettings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteSettings',
        ),
    ]
