
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs = Blog.objects #쿼리셋
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.order_by('-pub_data')
    #블로그 객체 세 개를 한 페이지로 자른다
    paginator = Paginator(blog_list, 5)
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts= paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def myhome(request):
    blogs = Blog.objects #쿼리셋
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.order_by('-pub_data')
    blog_list = Blog.objects.filter(username=request.user.username)
    #블로그 객체 세 개를 한 페이지로 자른다
    paginator = Paginator(blog_list, 5)
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts= paginator.get_page(page)
    return render(request, 'myhome.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')


def blogpost(request):
    if request.method == 'POST':
        one_memo=Blog()
        one_memo.title=request.POST['title']    
        one_memo.username=request.POST['username']
        one_memo.body=request.POST['content']
        one_memo.nickname=request.POST['nickname']
        one_memo.pub_data = timezone.now()
        if 'image' in request.FILES.keys():
            one_memo.image=request.FILES['image']
        one_memo.save()
        return redirect('home')
    # 2. 빈페이지를 띄워주는 기능 -> GET
    else:
        return render(request, 'new.html')

def update(request, pk):
    #어떤 블로그를 수정할 지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    #해당하는 블로그 객체의 pk에 맞는 입력공간을 가져오기
    blog.title=request.POST['title']
    blog.body=request.POST['content']
    blog.pub_data=timezone.now()
    if 'image' in request.FILES.keys():
        blog.image=request.FILES['image']
    blog.save()

    return redirect('home')




def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)#블로그모델에 해당하는 몇번째 데이터를, 블로그 변수에 담아주고
    blog.delete()
    return redirect('home')

def edit(request,blog_id):
    one_blog=get_object_or_404(Blog,pk=blog_id)
    return render(request,'edit.html',{'blog':one_blog})