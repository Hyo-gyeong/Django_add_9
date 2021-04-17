from django.db import models
from django.contrib.auth.models import User
#장고에서 구현해주고 있는 user불러오기
from django.urls import reverse
from django.conf import settings


class Photo(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  #Photo model을 user에 foreignkey로 연결 models.CASCADE : 외래키도 함께 삭제
  text = models.TextField(blank = True)
  image = models.ImageField(upload_to = 'timeline_photo/%Y/%m/%d')
  #ImageField :  FileField를 상속받은 필드이며, Pillow라는 따로 install 받은 이미지 처리 라이브러리를 통해서 이미지 정보를 획득.
  #*FileField : File Storage API를 통해 파일을 저장하며, django-storages를 통해 확장이 가능
  #upload_to : MEDIA_ROOT 하위에 저장할 파일,경로명 설정
  #timeline_photo폴더에 연도, 월, 일을 만들어서 사진을 저장 -> 년원일을 지정하면 파일끼리 충돌 방지 가능
  created = models.DateTimeField(auto_now_add = True) #최초 DB입력시간
  updated = models.DateTimeField(auto_now = True) #변화가 있을 때 즉, 수정했을 때의 시각

  #좋아요
  like = models.ManyToManyField(User, related_name='like')

  def __str__(self):
    return self.text

  class Meta:
    ordering = ['-created']

  #상세페이지로 이동하도록 absolute_url 설정 
  def get_absolute_url(self):
    return reverse('photo:detail', args=[self.id]) #이후에 views에서 return super가 나오게 되면 자동적으로 absolute_url 이 실행
