from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register simple models
admin.site.register(Genre)
admin.site.register(Language)

# Author Admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        ('General Information', {'fields': ('first_name', 'last_name')}),
        ('Dates', {'fields': (('date_of_birth', 'date_of_death'))}),
    )
admin.site.register(Author, AuthorAdmin)

# Inline for BookInstance in Book admin
class BooksInstanceInline(admin.StackedInline):
    model = BookInstance
    extra = 2
# Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre')
    inlines = [BooksInstanceInline]


# BookInstance Admin
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
