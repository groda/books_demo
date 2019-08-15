# Generated by Django 2.2.4 on 2019-08-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksdemo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='abstract',
            field=models.CharField(max_length=28000),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=140, primary_key=True, serialize=False),
        ),
    ]
