# Generated by Django 4.2.2 on 2023-06-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_payment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
