# Generated by Django 4.0.6 on 2022-07-31 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookAuthor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(related_name='book_author', to='appBookAuthor.authors'),
        ),
    ]
