# Generated by Django 3.2.7 on 2021-11-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0006_alter_price_history_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price_history',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
