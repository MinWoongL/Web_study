from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
      # widget : form이 지원하는 기본기능 이 외의 추가적인 동작을 원할 때 사용
#     content = forms.CharField(widget=forms.Textarea)

# 1. Form
# - 사용자의 입력을 개발자가 직접 구성
#   -> Model의 필드와 관계없이 마음대로 구성할 수 있다.
# - 장점: 내 마음대로 원하는 입력을 받을 수 있다.
# - 단점: DB에 정확히 저장하기 위해서 models를 완벽하게 파악하고 있어야한다.
#         models.py와 중복 코드가 많이 발생한다.

# 2. ModelForm
# - model에 정의된 필드만 입력 받을 수 있음
# - 장점: 사용법이 간단한다.
# - 단점: 사용자 마음대로 입력을 못 받는다.


class ArticleForm(forms.ModelForm):

    class Meta:
        # 특정 모델을 참조해야 한다.
        model = Article
        fields = "__all__" # 모든필드포함
        # fields = ('title', 'content', 'author',) -> 원하는 필드만 -> 무조건 튜플형태로 작성해야 함
        # exclude = ('title',) # 모델에서 포함하지 않을 필드 -> 튜플형태이려면 한 개여도 ',' 꼭 포함해서 작성
        # fields, exclude를 함께 사용해도 되지만 권장하지 않음