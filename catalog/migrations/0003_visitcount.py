# Generated by Django 2.0.6 on 2018-07-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180701_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit', models.IntegerField(default=0)),
            ],
        ),
    ]
