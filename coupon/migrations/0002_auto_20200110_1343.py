# Generated by Django 2.1 on 2020-01-10 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='use_form',
            new_name='use_from',
        ),
    ]