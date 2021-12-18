# Generated by Django 3.2.9 on 2021-12-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211216_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('surname', models.CharField(max_length=100)),
                ('hospital_name', models.CharField(max_length=100)),
                ('Doctorname', models.CharField(max_length=100)),
                ('bloodtype', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('len', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]