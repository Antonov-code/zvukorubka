# Generated by Django 5.1.5 on 2025-02-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rubka', '0003_voiceactor_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='comments',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
