# Generated by Django 3.2.12 on 2022-03-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('ISBN', models.CharField(default='', max_length=13, primary_key=True, serialize=False)),
                ('BookTitle', models.CharField(blank=True, max_length=255, null=True)),
                ('BookAuthor', models.CharField(blank=True, max_length=255, null=True)),
                ('YearOfPublication', models.IntegerField(blank=True, null=True)),
                ('Publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('ImageURLS', models.CharField(blank=True, max_length=255, null=True)),
                ('ImageURLM', models.CharField(blank=True, max_length=255, null=True)),
                ('ImageURLL', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('UserID', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default=123456, max_length=255)),
                ('Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='bookRatings',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('UserID', models.IntegerField(default=0)),
                ('ISBN', models.CharField(default='', max_length=13)),
                ('BookRating', models.IntegerField(default=0)),
            ],
            options={
                'unique_together': {('UserID', 'ISBN')},
            },
        ),
    ]
