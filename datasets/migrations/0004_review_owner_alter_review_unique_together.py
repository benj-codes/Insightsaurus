# Generated by Django 5.0.3 on 2024-04-10 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0003_dataset_dataset_image'),
        ('users', '0004_remove_profile_url_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'dataset')},
        ),
    ]
