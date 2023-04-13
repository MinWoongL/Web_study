# 커스텀 필터를 만들것
# content 를 받아와 해쉬태그만 a태그로 변경

# 필수 정의 영역
from django import template
from articles.models import Hashtag
# name으로 url을 알기 위해 사용
from django.shortcuts import resolve_url
# safe escape처리를 미리 해주기 위해 사용
from django.utils.safestring import mark_safe

register = template.Library()


# 내가 만든 커스텀 함수
# value: content가 넘어옴
# arg: 뒤에 작성한 내용
def cut(value, arg):
    # return '필터' -> content 전체가 필터 라는 글자로 바뀜
    return value.replace(arg, '')

# 데코레이터를 해주고 따로 등록하지않아도 등록한것처럼 동작
@register.filter
def set_hashtag(value):
    contents = value.replace('\r\n', ' ').split(' ')
    for i in range(len(contents)):
        if contents[i].startswith('#'):
            hashtag = contents[i][1:]
            # #으로 시작하는 모든 단어는 무조건 해시태그라는 확신이 있어야한다.
            try:
                hashtag_obg = Hashtag.objects.get(content=hashtag)
                # a 태그로 변경
                contents[i] = f'<a href="{resolve_url("articles:hashtag", hashtag_obg.pk)}">#{hashtag}</a>'
            # #으로 시작하지만 hashtag 테이블에 없는것은 pass로 처리 (에러 방지)
            except Hashtag.DoesNotExist:
                pass
    return mark_safe(' '.join(contents))

# 커스텀함수를 filter에 등록
register.filter('cut', cut)
register.filter('set_hashtag', set_hashtag)