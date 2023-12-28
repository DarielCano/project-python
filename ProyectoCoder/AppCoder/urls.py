from django.contrib import admin
from django.urls import path 
from .views import index, book, author, journal, publication, author_form,revista_form,libro_form,publicacion_form, search


urlpatterns = [
    path("",index, name="inicio"),
        path("book/",book,name="book"),
            path("author/",author,name="author"),
                path("journal/",journal, name="journal"),
                    path("publication/",publication, name="publication"),
                    path("authorform/",author_form,name="authorForm"),
                     path("journalform/",revista_form,name="journalForm"),
                      path("bookform/",libro_form,name="bookForm"),
                       path("publicationform/",publicacion_form,name="publicationForm"),
                        path("search/",search,name="search"),
]
