# Generated by Django 4.0.5 on 2022-06-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0010_rename_community_id_communitypost_community_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communitypost',
            old_name='user',
            new_name='creator',
        ),
    ]
