# Generated by Django 3.2.9 on 2021-12-16 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20211215_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bloodtype',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctorname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='len',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surname',
            field=models.CharField(max_length=100),
        ),
    ]