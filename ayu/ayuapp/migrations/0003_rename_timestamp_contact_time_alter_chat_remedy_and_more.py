# Generated by Django 4.2 on 2023-05-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayuapp', '0002_contact_alter_chat_remedy_alter_chat_symptoms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='timeStamp',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='chat',
            name='remedy',
            field=models.CharField(max_length=999),
        ),
        migrations.AlterField(
            model_name='chat',
            name='symptoms',
            field=models.CharField(max_length=999),
        ),
    ]
