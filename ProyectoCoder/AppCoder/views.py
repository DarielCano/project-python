from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from AppCoder.models import Book,Journal,Publication,Author



def index(request):
              
    return render(request,"index.html")
        


def book(request):
  books = Book.objects.all()  
  return render(request,"libro.html",{"books":books})
    
    
def author(request):
     authors = Author.objects.all()         
     return render(request,"autor.html", {"authors":authors})
        
   
def journal(request):
   journals = Journal.objects.all()
   return render(request,"revista.html", {"journals":journals})

def publication(request):
    publications= Publication.objects.all()
    return render(request,"publicacion.html", {"publications":publications})
    
    
def author_form(request):
     if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        publications =  request.POST.get("publications")
        
        newAuthor = Author(name= name,surname=surname,age=age,publications= publications)
        newAuthor.save()
            

        return render(request,"index.html")
     return render(request,"autor_form.html")   
   
  
def revista_form(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        author = request.POST.get("author")
        keywords =  request.POST.get("keywords")
        
        newJournal = Journal(title= title,year=year,author=author,keywords= keywords)
        newJournal.save()
            
        return render(request,"index.html")
    return render(request,"revista_form.html")   


def libro_form(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        author = request.POST.get("author")
   
        
        newBook = Book(title= title,year=year,author=author,)
        newBook.save()
            

        return render(request,"index.html")
    return render(request,"libro_form.html")   


def publicacion_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
               
        newPublication = Publication(name= name,author=author,isActive=True)
        newPublication.save()
         
        return render(request,"index.html")
    return render(request,"publicacion_form.html")   



def search(request):
     if request.method == "GET":
        search = request.GET.get("search")
        select = request.GET.get("select")
        if search:
            if select == "book":
               book = Book.objects.filter(title__icontains =search) 
               return render(request,"search.html",{"result":book,"select":select})
            elif select == "journal":
                 journal = Journal.objects.filter(title__icontains =search) 
                 return render(request,"search.html",{"result":journal,"select":select})
            elif select == "author":
                 author= Author.objects.filter(name__icontains =search) 
                 return render(request,"search.html",{"result":author,"select":select})
            else:
                 publication= Publication.objects.filter(name__icontains =search) 
                 return render(request,"search.html",{"result":publication,"select":select})
            
     
  
               
     
         
        return render(request,"index.html") 