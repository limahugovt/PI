# Generated by Django 5.0.3 on 2024-03-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='ano',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='livro',
            name='autor',
            field=models.CharField(max_length=255),
        ),
    ]