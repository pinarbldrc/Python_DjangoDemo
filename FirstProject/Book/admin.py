from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):


    list_display=["title","author"]
    list_display_links=["title"]
    search_fields=["author"]

    class Meta:
        model=Book

# Register your models here.
