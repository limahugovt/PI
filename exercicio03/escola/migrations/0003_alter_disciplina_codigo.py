# Generated by Django 5.0.3 on 2024-03-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("escola", "0002_disciplina"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disciplina",
            name="codigo",
            field=models.CharField(max_length=155),
        ),
    ]
