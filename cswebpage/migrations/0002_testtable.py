# Generated by Django 4.0.4 on 2022-04-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cswebpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testtable',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('test', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'testTable',
                'managed': False,
            },
        ),
    ]