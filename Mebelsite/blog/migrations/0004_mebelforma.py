# Generated by Django 4.0.5 on 2022-06-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mebelforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ism', models.CharField(max_length=100)),
                ('Tel', models.CharField(max_length=100)),
                ('Manzil', models.TextField()),
            ],
        ),
    ]
