# Generated by Django 4.2.8 on 2024-04-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_worksheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksheet',
            name='category',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='worksheet',
            name='file',
            field=models.FileField(upload_to='worksheets/'),
        ),
    ]
