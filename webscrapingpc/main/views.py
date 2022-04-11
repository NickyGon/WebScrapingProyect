from django.shortcuts import render
from django.http import HttpResponse
from itsdangerous import json
from . import scrap
from types import SimpleNamespace

def home(request):
    return render(request,'main/home.html',{"name":"Nuestro Producto"})
    
def nosotros(request):
    return render(request,'main/aboutus.html',{"name":"Sobre la app"})

def resultados(request):
    searched=''
    x=[]
    devolve=[]
    
    html=scrap.fetch_card_html()
    results=scrap.extract_card_info(html)
    if (results):
        scrap.saveToJson(results)
        #Para obtener el archivo como string de JSON, con open en "r" para solo leerlo
        f = open("cards.json", "r")
        #Para convertir nuestro string f en JSON, utilizando la librería SimpleNameSpace
        x = json.loads(f.read(), object_hook=lambda d: SimpleNamespace(**d))
    if request.method=="POST":
       searched= request.POST['searched']
       for it in x:
           if searched in it.name.lower():
               devolve.append(it)
         
    return render(request,'main/resultados.html',{'searched':searched, 'items':devolve})

    