# Generated by Django 4.1.4 on 2023-01-16 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_remove_snippet_grade_snippet_fr_snippet_jr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
