# Generated by Django 5.0.3 on 2024-03-27 18:18

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_num', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='dataset',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewBody', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Upvote'), ('down', 'Downvote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id_num', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.dataset')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(blank=True, to='datasets.tag'),
        ),
    ]
