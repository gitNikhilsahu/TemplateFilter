# Generated by Django 2.2.7 on 2019-12-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('subject', models.CharField(max_length=40)),
                ('dept', models.CharField(max_length=40)),
                ('date', models.DateField()),
            ],
        ),
    ]
