from .models import Author
from .models import Book
from .models import BookInstance
from .models import Genre
from .models import Profile

from django.contrib.auth import authenticate
from django.contrib.auth import  login
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

 
def index(request):
   
    num_books=Book.objects.all()

    num_books=num_books.count()

    num_instances=BookInstance.objects.all().count()

    num_instances_available=BookInstance.objects.filter(status='a').count()

    num_authors=Author.objects.all().count()

    num_genres=Genre.objects.all().count()

    num_readed=Profile.objects.filter(state__is_readed=True).count()

<<<<<<< HEAD
    num_visits=request.session.get('num_visits', 0)
    
    request.session['num_visits'] = num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
=======
>>>>>>> C8
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors,
                 'num_genres':num_genres,
                 'num_readed':num_readed,
                 'num_visits':num_visits},
    )

class BookListView(generic.ListView):
    
    model = Book
    paginate_by = 2 # se realiza la paginación para que no cargue todos los registros al tiempo y paginarlos, esto mejora el rendimiento
    #context_object_name = 'book'   # your own name for the list as a template variable
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    #queryset = Book.objects.filter(title__icontains='el')[:5] # Get 5 books containing the title war

    #def get_queryset(self): #esta función se encarga de obtener los objetos del modelo   # se está sobreescribiendo el el método
    #    return Book.objects.filter(title__icontains='ñ')[:5]# para cambiar la lista de registros devueltos.
                                                              # Esto es más flexible que simplemente ajustar 
                                                              # el atributo queryset
        
    #Podríamos también sobreescribir get_context_data() con el objeto de pasar variables de contexto adicionales a la plantilla 
    def get_context_data(self,**kwargs): # se usa con el objeto de pasar variables, de contexto adicionales 
        context=super(BookListView, self).get_context_data(**kwargs) #se trae el contexto existente 
        # *args se usa para que una función reciba una cantidad indefinida de argumentos, el * puede ser usada para pasarle los argumentos a una función 
        #**kwars recibe los argumento para almacenarlos con una clave. es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. Siendo esto así, el orden de los mismos es indistinto.  
        context["books"]=Book.objects.filter(title__icontains="el") # Get the blog from id and add it to the contex
        return context
        #Cuando se hace esto es importante seguir este patrón:
            #primero obtener el contexto existente desde nuestra superclase.
            #Luego añadir tu nueva información de contexto.
            #Luego devolver el nuevo contexto (actualizado).
        
class BookDetailView(generic.DetailView):
    model = Book
    paginate_by=1

class AuthorListView (generic.ListView):
    model= Author
    paginate_by=3

class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by=1
 
@login_required
def partida(request):
	logout(request)
	return render (request, 'registration/logged.html')
    #return redirect ('login')

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class AllBorrowedListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'catalog.can_mark_returned'
    model= BookInstance
    template_name='catalog/all_borrowed_books.html'
    paginate_by=10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o')

