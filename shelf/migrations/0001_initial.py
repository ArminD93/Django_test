# Generated by Django 2.0.3 on 2018-05-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer_Meteo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='SOME STRING', max_length=100)),
                ('answA', models.CharField(max_length=100)),
                ('answB', models.CharField(max_length=100)),
                ('answC', models.CharField(max_length=100)),
                ('answCorrect', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Meteo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('answA', models.CharField(max_length=100)),
                ('answB', models.CharField(max_length=100)),
                ('answC', models.CharField(max_length=100)),
                ('answCorrect', models.CharField(max_length=1)),
            ],
        ),
    ]
