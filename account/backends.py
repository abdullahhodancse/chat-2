
#for this code we can use email and password  for login not to use traditional username and pass for loging

from django.contrib.auth.backends import ModelBackend
from account.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None