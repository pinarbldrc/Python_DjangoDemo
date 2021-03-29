from django.db import models



class Book(models.Model):

    

    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    content=models.TextField(verbose_name="İcerik")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")

    def __str__(self):
        return self.title
    
    

# Create your models here.
