# Generated by Django 2.2.5 on 2019-09-21 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20190921_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_details',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'U'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
