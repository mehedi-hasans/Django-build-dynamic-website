# Generated by Django 4.2.6 on 2023-10-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='client/')),
            ],
        ),
    ]
