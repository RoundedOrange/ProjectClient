# Generated by Django 3.2 on 2023-07-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0003_auto_20230706_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=11),
        ),
    ]
