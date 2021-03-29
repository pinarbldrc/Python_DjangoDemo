from django.shortcuts import render,redirect
from .models import Article
from .forms  import ArticleForm

def listArticle(request):

    context=Article.objects.filter(yayinlanma_zamani__isnull=False)

    return render(request,"article/list.html",{"context":context})


def listAllArticle(requset):
    context=Article.objects.all()
    return render(requset,"article/allList.html",{"context":context})


def createArticle(request):

    if request.method=="POST":
        forms=ArticleForm(request.POST)
        if forms.is_valid():
            article=forms.save(commit=True)
            

    else:

      forms=ArticleForm()
    return render(request,"article/createArticle.html",{'forms':forms})

   #return redirect('listAllArticle/',)

     

#def articleDetail(request,id):
    #article=Article.objects.filter(id= id).first()
   # return render(request,"article/articleDetail.html",{"article":article})
