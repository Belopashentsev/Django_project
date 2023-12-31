from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("basketapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="basketitem",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_basket",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
