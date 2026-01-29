from django.shortcuts import render
from django.http import Http404
from todo.models import Todo

# render를 사용, todo의 제목을 템플릿에 전달하고 todo_list.html을 렌더링
def todo_list(request): # DB에서 todo들을 가져와서 목록페이지 넘기기
    todo_list = Todo.objects.all().values_list('id','title') # .values_list('','') -> 각 행을 튜플형태로 뽑기
    result = [{'id':todo[0], 'title':todo[1]} for i, todo in enumerate(todo_list)] # 리스트 컴프리핸션
    return render(request, 'todo_list.html', {'data':result})


# render를 사용, todo의 상세 정보를 템플릿에 전달하고 todo_info.html을 렌더링
def todo_info(request, todo_id): # 특정 id의 todo를 1개 가져와서 상세페이지 넘기기
    try:
        todo = Todo.objects.get(id=todo_id)
        info = {
            'title' : todo.title,               # info 라는 변수에 {...} 딕셔너리 객체 할당
            'description' : todo.description,
            'start_date' : todo.start_date,
            'end_date' : todo.end_date,
            'is_completed' : todo.is_completed,
        }
        return render(request, 'todo_info.html',{'data':info})
    except Todo.DoesNotExist:
        raise Http404("Todo가 존재하지 않습니다.")