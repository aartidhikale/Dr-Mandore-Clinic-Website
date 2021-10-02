# Generated by Django 3.0.7 on 2021-10-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_item1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=254)),
            ],
        ),
    ]
