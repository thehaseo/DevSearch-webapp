# Generated by Django 4.0.3 on 2022-04-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/default_ja1c8d.jpg', null=True, upload_to='images/'),
        ),
    ]
