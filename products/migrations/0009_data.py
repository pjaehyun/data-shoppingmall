# Generated by Django 3.1.3 on 2020-12-11 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20201119_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('desc', models.CharField(max_length=80)),
                ('data', models.FileField(upload_to='product_datas')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datas', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
