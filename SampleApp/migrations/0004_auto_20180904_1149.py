# Generated by Django 2.1.1 on 2018-09-04 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SampleApp', '0003_auto_20180904_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry_1',
            old_name='topic',
            new_name='Sample_obj1',
        ),
        migrations.RenameField(
            model_name='entry_2',
            old_name='topic',
            new_name='Sample_obj2',
        ),
    ]
