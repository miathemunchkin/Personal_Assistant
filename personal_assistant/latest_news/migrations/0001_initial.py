# Generated by Django 5.1 on 2024-08-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.TextField()),
                ('buy', models.DecimalField(decimal_places=2, max_digits=7)),
                ('sell', models.DecimalField(decimal_places=2, max_digits=7)),
                ('last_update', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.IntegerField(auto_created=True)),
                ('img_url', models.TextField()),
                ('title', models.TextField()),
                ('fulltext', models.TextField()),
                ('date', models.TextField()),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
    ]
