from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models



# custome user
class UserManager(BaseUserManager):
   
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    #super user create hobe 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        


        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True")
        return self.create_user(email, password, **extra_fields)
    


# here AbstractBaseUser,PermissionsMixin beacuse Core authentication fields & methods and Permission system & superuser support
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique = True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
     
     #databse  indexing for emmail firld for fast query
    class Meta:
        indexes = [models.Index(fields=['email'])]

    def  __str__(self):
        return self.email
    
    