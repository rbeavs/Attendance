# Generated by Django 4.1.4 on 2023-01-31 03:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0009_snippet_event_alter_snippet_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('events', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='snippet',
            old_name='SE',
            new_name='SR',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='event',
        ),
        migrations.AlterField(
            model_name='snippet',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 3, 1, 56, 568680, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='snippet',
            name='option',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='attendance.option'),
        ),
    ]