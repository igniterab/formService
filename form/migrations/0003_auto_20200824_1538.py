# Generated by Django 2.1.4 on 2020-08-25 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(default='Untitled Section', max_length=30),
        ),
    ]
