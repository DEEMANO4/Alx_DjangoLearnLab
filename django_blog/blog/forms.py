from django.contrib.auth.forms import UserCreationForm
from .models import POST

class PostRegistrationForm(UserCreationForm):
    class Meta:
        model = POST
        fields = ('email')