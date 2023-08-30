# Generated by Django 4.2 on 2023-05-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('symptoms', models.CharField(max_length=999)),
                ('remedy', models.CharField(max_length=999)),
            ],
            options={
                'db_table': 'chat',
            },
        ),
    ]