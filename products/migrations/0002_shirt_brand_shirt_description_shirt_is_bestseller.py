# Generated by Django 5.2 on 2025-04-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='brand',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shirt',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='shirt',
            name='is_bestseller',
            field=models.BooleanField(default=False),
        ),
    ]
