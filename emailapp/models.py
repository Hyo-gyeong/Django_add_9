from django.db import models


class Email(models.Model):
  title = models.CharField(max_length = 200)
  body = models.TextField(default="Django에서 보낸 메시지 입니다.")
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
