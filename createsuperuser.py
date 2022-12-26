from django.db import IntegrityError
from django.contrib.auth.models import User

try:
    superuser = User.objects.create_superuser(
        username="admin",
        email="abc@gmail.com",
        password="admin")
    superuser.save()
except IntegrityError:
    print(f"Super User is already exit!")
except Exception as e:
    print(e)
