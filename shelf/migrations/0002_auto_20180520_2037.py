# Generated by Django 2.0.3 on 2018-05-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer_meteo',
            name='id',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
    ]
