# Generated by Django 4.0.6 on 2022-07-18 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clothes", "0006_alter_cloth_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cloth",
            name="category",
            field=models.CharField(
                choices=[
                    ("Blazer", "Blazer"),
                    ("Cardigan", "Cardigan"),
                    ("Casual Trouser", "Casual Trouser"),
                    ("Formal Trouser", "Formal Trouser"),
                    ("Hoodie", "Hoodie"),
                    ("Jacket", "Jacket"),
                    ("Jeans", "Jeans"),
                    ("Polo shirt", "Polo shirt"),
                    ("Pullover", "Pullover"),
                    ("Shirt", "Shirt"),
                    ("Shorts", "Shorts"),
                    ("Sleeveless shirt", "Sleeveless shirt"),
                    ("Suit", "Suit"),
                    ("Tshirt", "Tshirt"),
                    ("Waistcoat", "Waistcoat"),
                    ("Coat", "Coat"),
                    ("Dress", "Dress"),
                    ("Kurta", "Kurta"),
                    ("Saree", "Saree"),
                    ("Sheath dress", "Sheath dress"),
                    ("Shrug", "Shrug"),
                    ("Skirt", "Skirt"),
                    ("Sweater", "Sweater"),
                    ("Tops", "Tops"),
                ],
                max_length=30,
            ),
        ),
    ]
