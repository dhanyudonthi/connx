# Generated by Django 5.0.1 on 2025-07-11 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unified_communications', '0014_webexaiagent_webexcontactcenter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salespricing',
            name='item_type',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
