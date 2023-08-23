# Generated by Django 4.2.4 on 2023-08-23 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sign_on_date', models.DateField()),
                ('sign_off_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SmartsheetData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sign_on_date', models.DateField()),
                ('sign_off_date', models.DateField()),
            ],
        ),
    ]