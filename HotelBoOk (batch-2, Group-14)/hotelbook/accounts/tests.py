from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User, auth
user=User.objects.get(username='addy')
print(user.password)