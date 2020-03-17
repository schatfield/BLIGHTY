# Generated by Django 3.0.4 on 2020-03-16 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blightyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patronpub',
            name='has_experience',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patronpub',
            name='is_visited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patronpub',
            name='is_wished',
            field=models.BooleanField(default=False),
        ),
    ]
