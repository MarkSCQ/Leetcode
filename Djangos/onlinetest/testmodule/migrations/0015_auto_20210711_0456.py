# Generated by Django 3.1.3 on 2021-07-11 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testmodule', '0014_auto_20210710_0415'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='CourseeName',
            new_name='CourseName',
        ),
    ]
