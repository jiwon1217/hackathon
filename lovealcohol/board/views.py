from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import post

def posthome(req):
    posts = post.objects #쿼리셋
    #블로그 모든 글들을 대상으로
    post_list = post.objects.order_by('-created_at')
    #블로그 객체 세 개를 한 페이지로 자른다
    paginator = Paginator(post_list, 5)
    #request된 페이지가 뭔지를 알아내고 (request 페이지를 변수에 담아내고)
    page = req.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts= paginator.get_page(page)
    return render(req,'boardhome.html',{'post': posts})

def postnew(req):
    return render(req,'postnew.html')

def postcreate(req):
    if req.method=='POST':
        one_memo=post()
        one_memo.title=req.POST['title']    
        one_memo.content=req.POST['content'] 
        one_memo.username=req.POST['username']
        one_memo.nickname=req.POST['nickname']
        if 'image' in req.FILES.keys():
                one_memo.image=req.FILES['image']
        one_memo.save()
    return redirect('/board')

def postedit(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    return render(req, 'postedit.html', {'post': pot})

def postshow(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    coments = pot.postcoment_set.all()
    return render(req,'postshow.html',{'post': pot,'coments':coments})

def postdelete(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    pot.delete()
    return redirect('/board')

def postupdate(req,post_id):
    pot = get_object_or_404(post, pk=post_id)
    pot.title = req.POST['title']
    pot.content = req.POST['content']
    if 'image' in  req.FILES.keys():  
        pot.image=req.FILES.get('image',False)
    pot.save()
    return redirect('/board/show/'+str(post_id))

def commentcreate(req,post_id):
    if (req.method == 'POST'):
        pot = get_object_or_404(post, id=post_id)
        pot.postcoment_set.create(title=req.POST['coment_content'],username=req.POST['username'])
        return redirect('/board/show/'+ str(post_id))

def commentdelete(req,post_id,comment_id):
    pot = get_object_or_404(post, pk=post_id)
    coments = pot.postcoment_set.get(id=comment_id)
    coments.delete()
    return redirect('/board/show/'+ str(post_id))

