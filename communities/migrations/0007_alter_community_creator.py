# Generated by Django 4.0.5 on 2022-06-06 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('communities', '0006_alter_communitypost_user_id_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='creator',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
