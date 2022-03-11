# Generated by Django 3.2.9 on 2022-03-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220308_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='current_period_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='有効期限'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='customer_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客ID'),
        ),
    ]
