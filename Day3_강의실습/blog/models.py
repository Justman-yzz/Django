from django.db import models

# 블로그 = 카테고리, 제목, 본문, (작성자), 작성일자, 수정일자, (썸네일이미지, 태그...)
class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('free', '자유'),
        ('oz_coding', '오즈코딩수업'),
        ('study_backend', '백엔드공부'),
        ('cook', '요리'),
        ('exercise', '운동'),
        ('baseball', '야구'),
        ('review', '회고'),
        ('read_book', '독서'),

    )
    category = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES) # select box를 자동으로 만들어주는 Django !!
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')

    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    def __str__(self):
        return f'[{self.get_category_display()}] {self.title[:15]}'

    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'


