# Generated by Django 5.1.5 on 2025-01-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_topic_cause_remove_topic_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='cause',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.TextField(default='Default description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='prevention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='symptoms',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='treatment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
