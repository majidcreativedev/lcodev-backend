from django.db import migrations
from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="Majid", email="mohammed.majid83@gmail.com",
                          is_staff=True, is_superuser=True, phone="9876543210", gender="Male")
        user.set_password("Waseem4*")
        user.save()
    dependencies = [

    ]
    operations = [
        migrations.RunPython(seed_data),
    ]
