from django.urls import reverse
from django.db import models
# 이 방법은 권장되는 방법이 아니다. 왜냐하면 User라는게 바뀔수도 있는데 이게
# 뭔가 자동동기화 되는 방식은 아닌듯 하다.
# from django.contrib.auth.models import User
# 때문에 settings에 AUTH_USER_MODEL이라는 영역에 User에 대한 설정값을 잡아주고, 수정도 거기서하고
# 임포트도 그것을 해온다.
from django.conf import settings


# Create your models here.

class Post(models.Model):
    # 만약 User를 임포트할것이라면 해당 임포트 경로를 임포트 해야하겠지만
    # 그렇지 않고도 사용가능한 방법은 어디 폴더에 속해있는지 명확히 알경우.
    # User의 경우 'auth.User'로 임포트 없이 사용이 가능하다.
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 이게 확인을 직접적으로 해봐야할 것같은데 비어있으면 디폴드 값이 false라고 한다.
    # 보통은 true가 아니던가
    # 따라서 만약 디폴드 값이 false가 되면 빈값을 허용하지 않는다. 라고 이해하면 될것같다.
    message = models.TextField()
    # upload_to를 해주지 않으면 사진파일등이 너무 많이 쌓이기 떄문에 (노드가 많이 쌓이기 때문에) upload_to를 지정해준다.
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    # ManyToManyField에서는 blank를 True로 하는것이 의미가 있다. (기본값은 False다)
    tag_set = models.ManyToManyField('Tag', blank=True)
    # 공개여부
    is_public = models.BooleanField(default=False, verbose_name='is_public')
    # auto_now_add는 데이터가 insert가 될때 자동으로 insert당시의 시각을 찍는다.
    # 따라서 admin페이지에서 찾아볼 수가 없다.
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now도 마찬가지로 입력을 할때 시간을 자동으로 찍어준다.
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString과 유사
    def __str__(self):
        # return f"Custom Post object({self.id})"
        return self.message

    # 모델 단에 구현할때
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = 'message number of characters'

    def get_absolute_url(self):
        return reverse('instagram:post_detail', args=[self.pk])

    # 자주 쓰이는 모델이라면 모델단에 구현하는게 맞다

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 다른 앱의 모델을 임포트할것이라면 instagram.Post라는 식으로 인자를 넣어줘서 사용이 가능하다.
    # post_id라는 필드가 생성이 된다.
    # limit_choices_to는 is_public이 True인것만 보여주겠다. 라는 의미이다
    # admin에서 포스트 수정 혹은 add를 할떄 limit_choices_to에 지정된 것대로 필터링이된 선택지가 제시된다.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, limit_choices_to={
        'is_public': True
    })
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
