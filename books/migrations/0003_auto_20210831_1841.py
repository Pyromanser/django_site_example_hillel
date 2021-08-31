# Generated by Django 3.2.6 on 2021-08-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='title'),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together={('first_name', 'last_name')},
        ),
    ]
