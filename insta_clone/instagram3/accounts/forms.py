from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class KoreanAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super(KoreanAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '사용자이름'
        self.fields['password'].label = '비밀번호'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
    
    def __init__(self, request=None, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = '사용자이름'
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'

        self.fields['username'].help_text = '150자 이하 문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
