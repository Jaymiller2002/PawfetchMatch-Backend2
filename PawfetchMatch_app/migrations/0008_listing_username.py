# Generated by Django 5.0.6 on 2024-06-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PawfetchMatch_app', '0007_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='username',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
