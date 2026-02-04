from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False) # 기본값은 False를 줘서 완료 후에 True변경하도록. 값을 안주면 null처리할수도 !! 일종의 안전장치
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self): # admin페이지 또는 shell에서 객체를 기계적인 표시가 아닌 self.title로 우리가 정의한 문자열을 보이게 해주기 !!
        return self.title