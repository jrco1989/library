from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

import uuid # Requerida para las instancias de libros únicos

class Genre(models.Model):
    types=models.CharField(
        max_length=200, 
        help_text="enter the genre of the book"
    )

    def __str__(self):
        #Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        #simplemente devuelve el nombre de un género definido por un registro en particular.
        # Como no hemos definido un nombre explicativo (verbose_name) para nuestro campo,
        # éste se establecerá en Name y se mostrará de esa manera en los formularios.
        return self.types
 
class Book(models.Model):
    title=models.CharField(
        max_length=100, 
        help_text="enter the book's name"
    )

    author = models.ForeignKey(
        'Author', 
        on_delete=models.SET_NULL, 
        null=True
    )

    #null=True, permite ingresar a la base de datos aun cuando el autor no ha sido seleccionado
    #on_delete=models.SET_NULL, pondrá el campo Null si el autor llega a ser elminado
    
    summary=models.TextField(
        max_length=1000, 
        help_text="insert a short description"
    )

    isbn = models.CharField(
        'ISBN',
        max_length=13, 
        help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    #isbn=models.Charfield(max_length=50, help_text="enter the ISBN  international standard book number,")
    
    genre=models.ManyToManyField(
        Genre, 
        help_text="Seleccione un genero para este libro"
    )

    language = models.ForeignKey(
        'Language', 
        on_delete=models.SET_NULL, 
        null=True
    )

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        # Devuelve el URL a una instancia particular de Book
        #en el administrador adiciona un vinculo sobre el nombre que añade los botones de delete, history  and view on site
        return reverse('book-detail', args=[str(self.id)])
    """
    devuelve un URL que puede ser usado para acceder al detalle de un registro particular
     (para que esto funcione, debemos definir un mapeo de URL que tenga el nombre book-detail
      y una vista y una plantilla asociadas a él) """
    
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        Esto crea una cadena con los tres primeros valores del campo genre (si existen) y crea una short_description 
        (descripción corta) que puede ser usada en el sitio de administración por este método.
        """
        return ', '.join([ genre.types for genre in self.genre.all()[:3] ])
   
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        help_text="ID único para este libro particular en toda la biblioteca"
    )

    book = models.ForeignKey(
        'Book',
        on_delete=models.SET_NULL,
        null=True
    )

    language = models.ForeignKey(
        'Language',
        on_delete=models.SET_NULL,
        null=True
    )

    imprint = models.CharField(
        max_length=200
    )
    
    due_back = models.DateField(
        null=True,
        blank=True
    )

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1, 
        choices=LOAN_STATUS, 
        blank=True, default='m', 
        help_text='Disponibilidad del libro'
    )
    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
   
    class Meta:
        ordering = ["due_back"]
        # El patrón metadata (Class Meta) usa este campo para ordenar 
        # registros cuando se retornan en una consulta.

        permissions = (("can_mark_returned", "Set book as returned"),) 

    def __str__(self):
        
        #return '%s (  %s) (  %s) (  %s)' % (self.id,self.book.title, self.book.author, self.language)
        return '{} {} {} {} ' .format(self.id,self.book.title, self.book.author, self.language)
        #El patrón __str__() representa el objeto BookInstance usando una 
        # combinación de  su id único y el título del  Book asociado
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

class Author(models.Model):

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    #nationality = models.CharField(max_length=100)
    
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )

    date_of_death = models.DateField(
        'Died', 
        null=True, 
        blank=True
    )
    
    #queda pendiente el ingreso de foto y otros detalles que se vayan ocurriendo.  
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo en administrador
        """
        #return '%s, %s' % (self.last_name, self.first_name)
        return '{}, {}'.format(self.last_name, self.first_name)

class Language(models.Model):

    idiom=models.CharField(
        max_length=20, 
        help_text='enter the language'
    )

    def __str__(self):
        return self.idiom

class Book_readed(models.Model):
    
    book_readed=models.OneToOneField(
        BookInstance,
        on_delete=models.CASCADE, 
        null=True
    )
    STATE_CHOICES = (
        (True, u'Yes'),
        (False, u'No'),
    )
    is_readed = models.BooleanField(
        verbose_name=u'Is it readed?',
        default=False,
        choices=STATE_CHOICES,
    )
    def __str__(self):
        return '{}: {}'.format(self.book_readed.book.title, self.book_readed.book.author)

class Profile (models.Model):
    
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    phone=models.CharField(
        blank=True, 
        max_length=12
    )
    state=models.ManyToManyField(
        Book_readed, 
        blank=True
    )
	#picture=models.ImageField(upload_to='user/imagens',blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self.user)