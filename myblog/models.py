from django.db import models

# Create your models here.
class Author(models.Model):
    '''
    author attributes are defined
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    '''
    categories are specified and creates a table
    '''
    catname = models.CharField(max_length=50)

    def __str__(self):
        return self.catname
    
class Tag(models.Model):
    tagname = models.CharField(max_length=50)

    def __str__(self):
        return self.tagname

class Post(models.Model):
    '''
    shows about title author etc in a post\
    '''
    title =models.CharField(max_length=100)
    body = models.TextField(max_length=50)
    created_date =models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    


