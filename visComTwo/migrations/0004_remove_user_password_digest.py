# Generated by Django 4.1.7 on 2023-03-06 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visComTwo', '0003_alter_communicationboard_visual_card_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password_digest',
        ),
    ]