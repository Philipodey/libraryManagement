# Generated by Django 5.0.4 on 2024-04-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
