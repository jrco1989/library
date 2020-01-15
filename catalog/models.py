from django.db import models
import uuid # Requerida para las instancias de libros únicos
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Genre(models.Model):
    types=models.CharField(max_length=200, help_text="enter the genre of the book")
    def __str__(self):
        #Cadena que representa a la instancia particular del modelo (p. ej. en el sitio de Administración)
        #simplemente devuelve el nombre de un género definido por un registro en particular.
        # Como no hemos definido un nombre explicativo (verbose_name) para nuestro campo, éste se establecerá en Name y se mostrará de esa manera en los formularios.
        return self.types
 
class Book(models.Model):
    title=models.CharField(max_length=100, help_text="enter the book's name")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    #null=True, permite ingresar a la base de datos aun cuando el autor no ha sido seleccionado
    #on_delete=models.SET_NULL, pondrá el campo Null si el auto llega a ser elminado
    summary=models.TextField(max_length=1000, help_text="insert a short description")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    #isbn=models.Charfield(max_length=50, help_text="enter the ISBN  international standard book number,")
    genre=models.ManyToManyField(Genre, help_text="Seleccione un genero para este libro")

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        # Devuelve el URL a una instancia particular de Book
        return reverse('book-detail', args=[str(self.id)]) #consultar a ivan 
    """
    devuelve un URL que puede ser usado para acceder al detalle de un registro particular
     (para que esto funcione, debemos definir un mapeo de URL que tenga el nombre book-detail
      y una vista y una plantilla asociadas a él) """

class BookInstance(models.Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, 
                                blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]
        # El patrón metadata (Class Meta) usa este campo para ordenar 
        # registros cuando se retornan en una consulta.

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)
        #El patrón __str__() representa el objeto BookInstance usando una 
        # combinación de  su id único y el título del  Book asociado

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)