from django.db import models

# Create your models here.
class Todo(models.Model):
    # django 에서 pk(id)는 자동으로 만들어준다.
    content = models.CharField(max_length=80)
    # default : 데이터를 생성할 때 값을 안넣으면 자동을 값을 채워서 데이터를 생성하겠다.
    completed = models.BooleanField(default=False)
