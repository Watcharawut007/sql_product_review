# Generated by Django 3.1.7 on 2021-03-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_production', '0002_auto_20210330_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Name_product',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='Id_review',
            new_name='review_id',
        ),
    ]
