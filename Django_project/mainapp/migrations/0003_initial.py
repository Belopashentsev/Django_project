from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_auto_20200912_2223"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name="productcategory",
            name="is_active",
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
