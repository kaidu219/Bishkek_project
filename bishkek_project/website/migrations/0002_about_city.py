# Generated by Django 4.1.6 on 2023-02-09 13:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_city',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('bloger_name', models.CharField(max_length=255)),
                ('text_article', models.CharField(max_length=500)),
                ('url_video', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]