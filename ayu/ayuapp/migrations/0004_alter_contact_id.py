# Generated by Django 4.2 on 2023-05-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayuapp', '0003_rename_timestamp_contact_time_alter_chat_remedy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]