# Generated by Django 3.0.7 on 2021-10-01 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consult1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('phone', models.TextField(max_length=254)),
                ('address', models.TextField(max_length=254)),
                ('Birthdate', models.TextField(max_length=254)),
                ('Birthmonth', models.TextField(max_length=254)),
                ('Birthyear', models.TextField(max_length=254)),
                ('Hobbies', models.TextField(max_length=254)),
                ('Diagnosis', models.TextField(max_length=254)),
                ('Work', models.TextField(max_length=254)),
                ('Diet', models.TextField(max_length=254)),
            ],
        ),
    ]
