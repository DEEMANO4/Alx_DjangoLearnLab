from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo):
        user = self.model(date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, date_of_birth, profile_photo):
        return super().create_superuser(date_of_birth,profile_photo)