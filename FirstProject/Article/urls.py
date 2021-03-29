from django.urls import path
from . import views

urlpatterns=[
    path('',views.listArticle,name="listArticle"),

    path('all/',views.listAllArticle,name="listAllArticle"),
    
    path('createArticle/',views.createArticle,name="createArticle"),

]