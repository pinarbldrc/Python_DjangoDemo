from django.db import models
from django.utils import timezone


class Article(models.Model):

    class Meta:
        verbose_name="makale"
        verbose_name_plural="makaleler"

    baslik=models.CharField(max_length=30)
    yazi=models.TextField()
    olusturma_zamani=models.DateTimeField(default=timezone.now)
    yayinlanma_zamani=models.DateTimeField(blank=True,null=True)
    secenekler=[("1","Deneme"),("2","Oyku"),("3","hikaye")]
    tur=models.CharField(max_length=5,choices=secenekler)

    def __str__(self):
        return self.baslik

    def yayinla(self):
        self.yayinlanma_zamani=timezone.now()
        self.save()
     



# Create your models here.
