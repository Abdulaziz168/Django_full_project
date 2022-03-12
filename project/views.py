from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    page = "projects"
    context = {'page':page}
    return render (request, 'projects.html',context)

def project(request,pk):
    return render (request, 'single-project.html')

 