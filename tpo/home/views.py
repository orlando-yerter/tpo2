from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post

# Create your views here.
def home(request):
    list_home = Post.objects.all()
    return render(request, 'home/base.html', {'list_home': list_home})