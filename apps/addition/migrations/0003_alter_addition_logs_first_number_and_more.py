# Generated by Django 4.1.7 on 2023-03-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0002_rename_logs_addition_logs_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addition_logs',
            name='first_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='addition_logs',
            name='result',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='addition_logs',
            name='second_number',
            field=models.IntegerField(),
        ),
    ]
