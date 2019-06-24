from django.contrib import admin

# Register your models here.
from home2.models import Book,Author,Genre,Customer

# Register your models here.

#admin.site.register(Book)

#admin.site.register(Author)
#admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    #note: RelatedOnlyFieldListFilter => applicable when some fields are related to other tables
    list_filter = ('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    list_filter = ('name','purchase_date','author')     

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('id','C_name')
    #note: RelatedOnlyFieldListFilter => applicable when some fields are related to other tables
    list_filter = ('C_name','C_purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    #list_filter = ('name','purchase_date','author')     
