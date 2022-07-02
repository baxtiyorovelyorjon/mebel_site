# Generated by Django 4.0.5 on 2022-06-08 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mebel_turi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategoriya', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mebel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Media/mebel_img')),
                ('mah_nomi', models.CharField(max_length=100)),
                ('narxi', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.brand')),
                ('kategoriya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.mebel_turi')),
            ],
        ),
    ]
