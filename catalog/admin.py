from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)
#admin.site.register(Author)
#admin.site.register(Book,BookAdmin)


class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance  

# Register the admin class with the associated model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

