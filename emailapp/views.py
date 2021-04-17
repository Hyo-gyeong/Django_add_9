from django.shortcuts import render
from django.core.mail.message import EmailMessage 
from .models import Email

def email_home(request):
  return render(request, 'index.html')

def send_email(request):
  sent = False
  if(request.method == 'POST'):
    post = Email()
    post.send_to = request.POST['send_to']
    post.title = request.POST['title']
    post.body = request.POST['body']  
    post.save()
    to = post.send_to.split(',')
    from_email = "dongdukmutsa@gmail.com"
    EmailMessage(subject=post.title, body=post.body, to=to, from_email=from_email).send()
    sent = True
    return render(request, "index.html", {"to":post.send_to, "sent":sent})