from django import forms
from .models import User
from django.contrib.auth.hashers import check_password

# class MultipleForm(forms.Form):
#     action = forms.CharField(max_length=60, widget=forms.HiddenInput())
#
# class SignupForm(MultipleForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]
#
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.save()
#
# class CheckPasswordForm(MultipleForm):
#     password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
#         attrs={'class': 'form-control',}),
#     )
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = self.user.password
#
#         if password:
#             if not check_password(password, confirm_password):
#                 self.add_error('password', '비밀번호가 일치하지 않습니다.')
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}),
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password

        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')

# cleaned_data로 form의 data 들고 옴