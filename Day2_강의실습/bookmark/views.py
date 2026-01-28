from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from bookmark.models import Bookmark

def bookmark_list(request):
    # 객체 묶음을 for로 하나씩 꺼내 HTML문자열로 만들어 누적 출력
    # bookmarks = Bookmark.objects.all()
    bookmarks = Bookmark.objects.filter(id__gte=50)
    lis = ""
    for b in bookmarks:
        lis += f'<li><a href="/bookmark/{b.pk}/">{b.name}</a></li>'
    return HttpResponse(f'<h1>북마크 리스트 페이지입니다.</h1><ul>{lis}</ul>')

def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)

    return HttpResponse(f'<h1>북마크 {pk}번 {bookmark.name}페이지 입니다 </h1>'
                        f"<p>URL: <a href='{bookmark.url}' target='_blank'>{bookmark.url}</a></p>"
                        )