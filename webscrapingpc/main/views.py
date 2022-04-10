from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'main/home.html',{"name":"Seware"})

def resultados(request):
    if request.method=="POST":
        searched= request.POST['searched']
        return render(request,'main/resultados.html',{'searched':searched})
    else:
        return render(request,'main/resultados.html',{})
    