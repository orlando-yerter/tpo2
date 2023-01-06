from django.shortcuts import render
from django.http import HttpResponseRedirect
from post.models import Post
from post.forms import PostForm

# Create your views here.
def edit(request):
    list_edit = Post.objects.all()
    return render(request, "edit/edit.html", {'list_edit': list_edit})

def edit_item(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            #si saco ese print form, no me cambia las imagenes.
            #un hechicero lo hizo (?
            print(form) 

            post.save()
            return HttpResponseRedirect('/edit')
    else:
        form= PostForm(instance=post)
        return HttpResponseRedirect('/home')
