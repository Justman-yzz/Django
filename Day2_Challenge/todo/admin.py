from django.contrib import admin
from todo.models import Todo

@admin.register(Todo) # Todo 모델을 admin에 등록하기 -> 이 클래스는 Todo의 관리자 설정이다 !!!
class TodoAdmin(admin.ModelAdmin): # Django 관리자 화면을 내가 원하는 방식으로 꾸미는 설정. 보고 조작하는 방식을 admin에서 규칙으로 지정.
    list_display = ('title', 'description', 'is_completed', 'start_date', 'end_date',) # 리스트에서 어떤 컬럼 보여줄래
    list_filter = ('is_completed',) # 필터 어떻게 할래 ### 튜플 끝에 , 를 붙여서 튜플 확실히 만들기 !!!!!
    search_fields = ('title',) # 검색 어떻게 할래
    ordering = ('start_date',) # 정렬 어떻게 할래
    fieldsets = (               # 읽기 쉬운 방식으로 폼을 구조화하기 -> 필드를 어떤 그룹으로 묶어 보여줄래
         ('Todo Info', {
            'fields': ('title', 'description', 'is_completed')
         }),
        ('Date Range', {
            'fields': ('start_date', 'end_date')
        }),                                         # 기본 편집 폼은 필드가 그냥 쭉 나열
    )
