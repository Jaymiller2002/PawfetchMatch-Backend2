# Generated by Django 5.0.6 on 2024-06-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PawfetchMatch_app', '0005_alter_listing_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
