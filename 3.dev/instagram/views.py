from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, Http404
from django.views.generic import ListView, DetailView

from .models import Post
# Create your views here.


post_list = ListView.as_view(model=Post)

'''
def post_list(request):
    qs = Post.objects.all()
    # GET이라는 속성중에서 (GET과 get의 의미는 여기서 다름. GET은 호출(request)타입이고 get은 일종의
    # "찾아줘"라는 의미라고 보면 된다.
    # 아무튼 q라는 문자가 들어있는것을 찾아줘 아니면 공백을 출력해줘 라는 의미다.)
    q = request.GET.get('q', '')

    if q:
        qs = qs.filter(message__icontains=q)
    # render에서 request 다음에 쓰인경로는 -> 이렇게된다. instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        # 여기서의 post_list는 추후 html로의 mapping 할때 활용이 된다.
        # 추가적으로는 확실치는 않지만 render에서 request 이후에 써준 경로에 뿌려지는 mapping 같기도 하다
        'post_list': qs,
        'q': q
    })
'''

"""
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:

    # response = HttpResponse()
    # response.write("Hello World")
    # response.write("Hello World")
    # response.write("Hello World")
    # response.write("Hello World")

    # 1 먼저있는 pk는 필드의 타입을 지정한 것이고
    # 1 뒤에 나오는 pk는 post_detail에서 인자로 받게된 값이다.
    # 2 추가로 이대로 그냥쓰게 되면 데이터 값이 없는경우에 500에러를 전송하게 된다.
    # 2 하지만 데이터가 없는게 서버에러는 아니기에 400에러로 변경시켜주기 위해서 try 구문을 사용해준다.
    # 3 하지만 이것조차 너무 길다.
    # 3 따라서 try, except 구문을 주석처리해주고 get_object_or_404로 처리한다.
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'instagram/post_detail.html', {
        # 'post'는 여기 render에서 지정된 post_detail.html로 보내주는 django-html용 태그다
        'post': post
    })
    # return response
"""
# 위의 post_detail을 이 한줄코드로 표현한다;
post_detail = DetailView.as_view(model=Post)

# request이후에 오는 year같은것들은 하나의 카테고리인데도
# 딱 하나만 사용하는게 아니라 변동이 있는경우에는 request외의 인자로도 받아서
# 어떤 값으로 사용한다. 출력을 위한 재료이거나 아니면 그 자체로 출력이 되든가.


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
