from django.urls import path
from . import views

urlpatterns=[
    path('about/',views.about,name="about"),

    #path('detail/<int:id>',views.detail,name="detail"),
    
    #path('createArticle/',views.createArticle,name="createArticle"),

]