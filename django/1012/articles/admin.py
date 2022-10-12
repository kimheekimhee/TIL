# articles/admin.py 을 아래와 같이 변경

from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


admin.site.register(Article, ArticleAdmin)

# 여기까지 작성하고 http://127.0.0.1:8000/admin/ 에 로그인해보면
# Article objects 라고 표시되던 컨텐츠들이
# 전부 각각의 제목, 작성시간, 수정시간으로 표시되고 있음을 확인 가능
