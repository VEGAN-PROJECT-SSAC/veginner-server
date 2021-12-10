from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

class UserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['nickname']