from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['baslik','yazi','olusturma_zamani','tur','yayinlanma_zamani']





 