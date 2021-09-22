from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
#django.views.generic
#제네릭뷰란 장고에서 기본적으로 제공하고 있는 뷰의 형태로, 개발할 때 자주 등장하는 내용을 모아놓은 뷰를 뜻한다. 개발의 속도를 더욱 빠르게 만들어주어 편리하게 개발할 수 있다는 장점이 있다.
#종류도 다양함 - 찾아보는것 추천!
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from .models import Photo
import json

class PhotoList(ListView):
  model = Photo
  template_name_suffix = '_list' #사용하는 탬플릿 명을 '모델명_list.html'로 바꾼다는 의미.
                                #해당 기능 완료후 연결될 템플릿 이름

class PhotoCreate(CreateView):
  model = Photo
  fields = ['text', 'image'] #생성시 채워야할 필드
  template_name_suffix = '_create'
  success_url = '/' #성공후 메인 페이지로 돌아가도록 연결(이후 url로 연결)

  #생성시 user 확인
  def form_valid(self, form):
    form.instance.author_id = self.request.user.id
    if form.is_valid():
      form.instance.save()
      return redirect('/')
    else:
      return self.render_to_response({'form':form}) 

class PhotoUpdate(UpdateView):
  model = Photo
  fields = ['text', 'image']
  template_name_suffix = '_update'
  #success_url = '/'

  def dispatch(self, request, *args, **kwargs): #사용자가 접속하였을 때 get이냐, post이냐를 결정하고 분기를 자동으로 해줌
    object = self.get_object()
    if object.author != request.user:
      messages.warning(request, '수정할 권한이 없습니다.')
      return HttpResponseRedirect('/')
    else:
      #super을 써줘서 원래 Updateview가 실행되도록 해주며 super을 쓰게 되면 실행시 absolute_url로 자동적으로 이동한다. (단 success url이 설정되어 있으면 우선시 된다.)
      return super(PhotoUpdate, self).dispatch(request, *args, **kwargs)

def delete(request, post_id):
    post = Photo.objects.get(id=post_id)
    post.delete()
    return redirect('/')

class PhotoDetail(DetailView):
  model = Photo
  template_name_sufffix = '_detail'


def post_likes(request): 
  if request.is_ajax(): #ajax 방식일 때 아래 코드 실행
    blog_id = request.GET['blog_id'] #좋아요를 누른 게시물id (blog_id)가지고 오기
    post = Photo.objects.get(id=blog_id) 
    
    user = request.user #request.user : 현재 로그인한 유저
    if post.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
      post.like.remove(user) #like field에 현재 유저 추가
      message = "좋아요 취소" #화면에 띄울 메세지
    else: #좋아요를 누르지 않은 유저일 때
      post.like.add(user) #like field에 현재 유저 삭제
      message = "좋아요" #화면에 띄울 메세지
      #post.like.count() : 게시물이 받은 좋아요 수  
  context = {
    'like_count' : post.like.count(),
    'message':message,
  }
  return HttpResponse(json.dumps(context), content_type='application/json')   