# Generated by Django 2.0.7 on 2019-02-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mymodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
            ],
        ),
    ]
