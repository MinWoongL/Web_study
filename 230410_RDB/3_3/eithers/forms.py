from .models import Question, Comment
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        labels = {
            'issue_a' : 'RED_TEAM',
            'issue_b' : 'BLUE_TEAM',
        }

class CommentForm(forms.ModelForm):
    # pick -> RED TEAM 선택 시 0 저장, BLUE TEAM 선택 시 1 저장
    pick = forms.ChoiceField(choices=[('0','RED TEAM'), ('1', 'BLUE TEAM')])
    class Meta:
        model = Comment
        exclude = ('question',)
        