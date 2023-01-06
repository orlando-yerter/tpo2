from django.shortcuts import render
from django.http import HttpResponseRedirect
from post.models import Post

# Create your views here.
def remove(request):
    list_remove = Post.objects.all()
    return render(request, "remove/remove.html", {'list_remove': list_remove})

def remove_item(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return HttpResponseRedirect('/remove')
    else:
        return HttpResponseRedirect('/home')

