from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag

# Register your models here.

# 방법1
# admin.site.register(Post)

# 방법2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 방법3
# 기본적으로 인자에 들어가는 models.py의 class를 넣게 되면 아래 admins.py에서
# class를 정의할때 각 변수에 1)모델단의 2)register에 들어가게된 클래스의 안에 있는 내용을
# 3) 변수의 인수로 사용할 수 있게된다.


@admin.register(Post)  # Wrapping (감싼 대상의 기능을 변경할 수 있다.)
class PostAdmin(admin.ModelAdmin):
    # 이거는 admin 관리창에서 볼 수 있는 카테고리라고 보면 된다.
    # *매우중요 그리고 list_display등에 대한 이름은 내 임의로 설정하는 것은 아닌듯 하고 어떤 특정 고정값인것같다.
    list_display = ['id', 'photo_tag', 'message',
                    'message_length', 'is_public', 'created_at', 'updated_at']
    # 기본 디폴트는 가장 처음 값에 해당하는 id에 링크가 걸리지만 이렇게 해주면 설정된 값이 링크로써 작용하게 된다.
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            # 기본적으로는 보안상의 문제때문에 전체를 보여주지 않는다.
            # 때문에 mark_safe를 해준다. 안전하다고, 그러면 노출이 되는 구조 같다.
            return mark_safe(f'<img src="{post.photo.url}" style="width: 75px;>')
        return None

    # 모델단에서 구현이 되었던 것을 어드민 단인 여기에 구현

    def message_length(self, post):
        return f"{len(post.message)} number of characters"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
