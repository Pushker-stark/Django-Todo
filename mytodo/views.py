from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MyTodo
# Create your views here.
def Home(request):
    # to send data to frontend from db
    if request.method == "POST":
        title=request.POST.get('title')
        if title != "":
            MyTodo.objects.create(title=title)
        return redirect('Home')
    all_data=MyTodo.objects.all()
    data={"data":all_data}
    return render(request,'home.html',context=data)

def Delete(request,id=None):
    MyTodo.objects.get(id=id).delete()
    return redirect('Home')

def Complete(request,id=None):
    data=MyTodo.objects.get(id=id)
    data.complete=True
    data.save()
    return redirect('Home')

def UnComplete(request,id=None):
    data=MyTodo.objects.get(id=id)
    data.complete=False
    data.save()
    return redirect('Home')
