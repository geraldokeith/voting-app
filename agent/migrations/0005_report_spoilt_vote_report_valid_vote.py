# Generated by Django 5.2.3 on 2025-06-24 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_candidate_passport_candidate_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='spoilt_vote',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
        ),
        migrations.AddField(
            model_name='report',
            name='valid_vote',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=100),
        ),
    ]
