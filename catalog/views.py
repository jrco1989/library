from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all()
    num_books=num_books.count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status='a').count()
    num_authors=Author.objects.all().count()
    num_genres=Genre.objects.all().count()
    
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors,
                 'num_genres':num_genres},
    )

class BookListView(generic.ListView):
    
    model = Book
    paginate_by = 2 # se realiza la paginación para que no cargue todos los registros al tiempo y paginarlos, esto mejora el rendimiento
    #context_object_name = 'book'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='c')[:5] # Get 5 books containing the title war
    #"""def get_queryset(self): #esta función se encarga de obtener los objetos del modelo
    #x    return Book.objects.filter(title__icontains='el')[:5]# para cambiar la lista de registros devueltos.
                                                              # Esto es más flexible que simplemente ajustar 
                                                              # el atributo queryset
    #template_name = 'book_list.html'  # Specify your own template name/location"""

    def get_context_data(self,**kwargs): # se usa con el objeto de pasar variables, de contexto adicionales 
        context=super(BookListView, self).get_context_data(**kwargs) #se trae el contexto existente 
        # *args se usa para que una función reciba una cantidad indefinida de argumentos, el * puede ser usada para pasarle los argumentos a una función 
        #**kwars recibe los argumento para almacenarlos conuna clave. es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. Siendo esto así, el orden de los mismos es indistinto.  
        context["books"]=Book.objects.filter(title__icontains="el")
        return context


class BookDetailView(generic.DetailView):
    model = Book
        

