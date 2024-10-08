# Generated by Django 4.2 on 2024-09-13 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus', '0004_rename_description_service1_description1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='reviewers/')),
                ('review_text', models.TextField()),
            ],
        ),
    ]
