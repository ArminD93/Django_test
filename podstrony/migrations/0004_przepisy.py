# Generated by Django 2.0.3 on 2018-06-09 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podstrony', '0003_teoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Przepisy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podstrony.Reporter')),
            ],
        ),
    ]
