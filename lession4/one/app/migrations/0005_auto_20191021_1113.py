# Generated by Django 2.1.2 on 2019-10-21 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='create_time',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='diary',
            name='content',
            field=models.TextField(max_length=800),
        ),
    ]