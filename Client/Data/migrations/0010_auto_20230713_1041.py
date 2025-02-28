# Generated by Django 3.2 on 2023-07-13 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data', '0009_auto_20230708_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='device',
            new_name='cluster',
        ),
        migrations.AddField(
            model_name='task',
            name='log_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='open_source',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='parameter_file_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='safety',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='use_fed_model',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='total_size',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
