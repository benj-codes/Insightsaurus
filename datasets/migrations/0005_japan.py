# Generated by Django 5.0.3 on 2024-04-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0004_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Japan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('birth_total', models.PositiveIntegerField()),
                ('birth_male', models.PositiveIntegerField()),
                ('birth_female', models.PositiveIntegerField()),
                ('birth_rate', models.FloatField()),
                ('birth_gender_ratio', models.FloatField()),
                ('population_total', models.PositiveIntegerField()),
                ('population_male', models.PositiveIntegerField()),
                ('population_female', models.PositiveIntegerField()),
            ],
        ),
    ]
