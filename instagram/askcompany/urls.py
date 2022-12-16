"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.conf import global_settings와
# from askcompany import settings를 합쳐준 개념이 아래에 있는 import이다.
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

class RootView(TemplateView):
    template_name = 'root.html'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='root.html'), name='root'),
    # 위의 RootView와 함께 쓸때
    # path('', RootView.as_view(), name='root'),
    # 이렇게 RedirectView를 해주게 되면 ''과 같이 지정된 페이지로 이동했을때 as_view안의 인자로
    # 들어있는 url이 붙어서 이동되게 된다.
    path('', RedirectView.as_view(
        # /url='/instagram/'
        # reverse url 사용
        # instagram urls에 들어있는 인자중 name이 post_list로 지정된 것을 찾아서 거기로 이동한다..
        pattern_name = 'instagram:post_list'
        ), name='root'),
    path('admin/', admin.site.urls),
    path('blog1/', include('blog1.urls')),
    path('instagram/', include('instagram.urls')),
    path('accounts/', include('accounts.urls')),
]

# debug 관련하여는 https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# 라는 공식문서를 참조하자.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
    