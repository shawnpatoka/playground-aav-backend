# Generated by Django 4.0.6 on 2023-04-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
