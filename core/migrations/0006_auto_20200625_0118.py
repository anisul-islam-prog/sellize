# Generated by Django 3.0.6 on 2020-06-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200625_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('OW', 'Outwear'), ('SW', 'Sports Wear'), ('S', 'Shirt')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('p', 'primary')], max_length=1),
        ),
    ]