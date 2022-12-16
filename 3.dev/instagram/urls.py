from django.urls import path, re_path, register_converter

from . import views


# Url reverse에서 names
app_name = 'instagram'

# 이건 정규표현식을 계속 쓰는 번거로움을 제거하기 위한 클래스다.


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # return "%04d" % value
        return str(value)


# 이거 자체가 일종의 path의 보조적 역할을 하는 것 같다.
register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('<str:pk>/', views.post_detail_2),
    path('<int:pk>/', views.post_detail),
    # year나 위의 pk처럼 단 하나의 값으로 지정되지 않았을 경우에는 그 입력하게될 타입에 따라서
    # int나 str등을 부여하게되고 이는 다시 views에서 request 바로 다음으로 이어받는 인자로 사용하게 된다.
    # path('archives/<int:year>/', views.archives_year)

    # 이거는 정규표현식에 의하여 좀 더 제한적으로 값을 사용하고 싶을때 사용할 수 있다.
    # re_path는 정규표현식으로 urls를 설정하는 짝궁이라고 생각하면 된다.
    # 맨 앞에 쓰인 r의 경우에는 백슬래시에 대해서 두번써주지 않고도 인식될 수 있는 기능을 한다.
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year)
    # {4}안에 들어간 숫자만큼 year로 받는 인자의 갯수를 지정한다.
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year)

    # YearConverter class와 register_converter를 정의 한 후에 사용해주는 path
    path('archives/<year:year>/', views.archives_year)
]
