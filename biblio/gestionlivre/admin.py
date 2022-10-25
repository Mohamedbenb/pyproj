from django.contrib import admin
from .models import Book,Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "price")
    list_editable = ("title", )
    list_display_links = ("price", )
    search_fields = ("title", )
    list_filter = ("category", )
    list_per_page = 10