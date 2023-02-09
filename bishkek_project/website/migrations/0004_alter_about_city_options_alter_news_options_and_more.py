# Generated by Django 4.1.6 on 2023-02-09 14:23

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_news_title_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_city',
            options={'verbose_name': 'About_city', 'verbose_name_plural': 'About_city'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
        migrations.AddField(
            model_name='about_city',
            name='title_article',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='correspondent_fname',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('', 'Культура'), ('', 'Интернет'), ('', 'Наука и технологии'), ('', 'Некрологи'), ('', 'Общество'), ('', 'Политика'), ('', 'Преступность и право'), ('', 'Проишествия'), ('', 'Рейтинги'), ('', 'Религия'), ('', 'Дни рождения'), ('', 'Спорт'), ('', 'Экономика')], max_length=255),
        ),
    ]