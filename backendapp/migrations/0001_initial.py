# Generated by Django 4.2.3 on 2024-12-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Businessregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('workspace_name', models.CharField(max_length=255)),
            ],
        ),
    ]
