# Generated by Django 4.2.2 on 2023-06-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_payment_amount_payment_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='razorpay_payment_id',
        ),
    ]
