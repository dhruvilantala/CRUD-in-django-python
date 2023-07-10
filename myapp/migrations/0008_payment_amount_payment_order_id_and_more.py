# Generated by Django 4.2.2 on 2023-06-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_payment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
