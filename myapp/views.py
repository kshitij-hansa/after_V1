from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse
from myapp.models import Blog

# Create your views here.
def index(request):
    return render(request,'index.html')

def Def(request):
    return HttpResponse("this is not for this page")

def page1(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'page1.html',context)

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def Search(request):
    return render(request,'search.html')