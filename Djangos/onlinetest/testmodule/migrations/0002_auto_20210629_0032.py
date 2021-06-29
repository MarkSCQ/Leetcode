# Generated by Django 3.1.3 on 2021-06-29 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.CharField(blank=True, choices=[('STU', 'Student'), ('STA', 'Staff'), ('TEA', 'Teacher')], default=None, max_length=20, null=True, verbose_name='Identification'),
        ),
    ]