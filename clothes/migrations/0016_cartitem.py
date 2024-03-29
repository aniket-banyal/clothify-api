# Generated by Django 4.0.6 on 2022-08-17 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0015_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cart')),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clothes.cloth')),
            ],
        ),
    ]
