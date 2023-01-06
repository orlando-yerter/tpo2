from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm

def post(request):
    if request.method == 'POST':
        # tuve que agregar request.FILES para que permita
        # subir archivos al ejecutar el submit
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            publi = form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = PostForm()
    return render(request, 'post/formulario.html',{'form': form})