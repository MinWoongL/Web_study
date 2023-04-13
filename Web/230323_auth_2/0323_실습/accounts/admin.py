from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

# UserAdmin : User 데이터를 입력받는 Form
# 관리자페이지에서 보이는 필드 수정하기
# 오버라이딩을 통해서 한다.
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "nickname")
    add_fieldsets=(
        (
            None,
            {
                "classes":("wide",),
                "fields": ("username", "password1", "password2", "nickname")
            },
        ),
    )
#admin.site.register(User)
admin.site.register(User, CustomUserAdmin)
# 두번째인자로 UserAdmin을 넣어줘야 내가 커스터마이징한 유저모델을 적용할 수 있다(?)