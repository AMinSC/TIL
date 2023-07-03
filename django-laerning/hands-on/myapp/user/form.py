from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import User
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', )


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        # models 에서 이미 설정을 해뒀기 때문에 아래는 주석 처리
        # fields = ['email', 'password']
        # widgets = {
        #     'email': forms.EmailInput(attrs={'placeholder': 'email'}),
        #     'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
        # }
