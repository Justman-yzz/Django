from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from blog.models import Blog
from django.views.decorators.http import require_http_methods, require_POST


def blog_list(request):
    blogs = Blog.objects.all()

    ## 쿠키로 방분 횟수 세기. 방문횟수 = (쿠키저장된 방문횟수) + 1
    # get으로 가져오는 것은 visits이라는 키값으로 가져오기
    # none값일 경우 0이라는 기본값 사용. 거기다 1 더하기
    # return값의 경우, string이므로 int 변환 !!
    visit = int(request.COOKIES.get('visit', 0)) + 1

    # 세션 id는 키값이라 어떤 정보도 알아낼 수 없음. 하지만 count는 계속 들어감.
    # 출력하지 않으면 세션 id를 알더라도 어떤 정보인지 클라이언트에서 확인 불가
    request.session['count'] = request.session.get('count', 0) + 1

    context = {
        'blogs': blogs,
        'count': request.session['count'],
    }

    response = render(request, 'blog_list.html', context)

    # set cookie하며 vistis라는 이름으로 visits가 가진 숫자 담기
    response.set_cookie('visit', visit)

    return response

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    context = {
        'blog': blog
    }
    return render(request, "blog_detail.html", context)

# 회원가입(폼 없이, create_user 사용)
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()

    if not username or not password:
        return render(request, "signup.html", {'error': '입력값이 비어있습니다.'})

    if User.objects.filter(username=username).exists():
        return render(request, "signup.html", {'error': '이미 존재하는 아이디입니다.'})

    # *** create_user가 비번 해싱까지 처리
    User.objects.create_user(username=username, password=password)
    return redirect("login")

# 로그인(authenticate -> login)
@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()

    user = authenticate(request, username=username, password=password)
    if user is None:
        return render(request, "login.html", {'error': '아이디 또는 비밀번호가 틀렸습니다.'})

    login(request, user) # 세션 생성 + sessionid 쿠키 세팅
    return redirect('/') # 홈에서

# 로그아웃
@require_http_methods(['GET', 'POST'])
def logout_view(request):
    logout(request) # 세션 끊기
    return redirect('blog_list')


