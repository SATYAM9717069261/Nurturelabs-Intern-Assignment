# Generated by Django 3.2.2 on 2021-05-09 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServerSide', '0004_remove_advisor_photourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bookingTime',
            field=models.DateTimeField(),
        ),
    ]
