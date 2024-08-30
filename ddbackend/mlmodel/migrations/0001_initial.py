# Generated by Django 4.1.9 on 2023-09-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bmi', models.FloatField()),
                ('health_risk', models.CharField(max_length=100)),
                ('bmi_category', models.CharField(max_length=100)),
                ('precautions', models.TextField()),
                ('probable_diseases', models.TextField()),
            ],
        ),
    ]
