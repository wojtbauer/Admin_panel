# Generated by Django 2.1.1 on 2018-09-04 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0002_entry_1_entry_2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry_1',
            options={'verbose_name_plural': 'entries_1'},
        ),
        migrations.AlterModelOptions(
            name='entry_2',
            options={'verbose_name_plural': 'entries_2'},
        ),
    ]