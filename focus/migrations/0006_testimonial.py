# Generated by Django 4.2 on 2024-09-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0005_customerreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_image', models.ImageField(upload_to='clients/')),
                ('client_business', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
