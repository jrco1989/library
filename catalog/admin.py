from django.contrib import admin
from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre
from .models import Language


#admin.site.register(Author)
# Define the admin class Para cambiar la forma en la que un modelo
#  se despliega en la interfaz de administración
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]# no se actualizó com se esperaba 
                                                                            #debería verse un despliegue en vertical 


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')



#admin.site.register(BookInstance)
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('status','due_back')
    list_filter = ('status', 'due_back') #para filtrar los campos 




admin.site.register(Genre)
admin.site.register(Language)
