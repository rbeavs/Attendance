# Generated by Django 4.1.4 on 2023-01-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_snippet_delete_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='grade',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SE', 'Senior')], max_length=4),
        ),
    ]
