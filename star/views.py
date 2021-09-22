from django.shortcuts import render
from .models import Rating
# Create your views here.

def index(request):
  obj = Rating.objects.all()
  return render(request, 'star/index.html', {'obj':obj})
