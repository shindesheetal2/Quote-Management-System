from django.db import models
from django.core.exceptions import ValidationError


class Author(models.Model):
    '''Model of Author'''
    name = models.CharField(max_length=20)
    dateofbirth = models.DateField()

    def __str__(self):
        return self.name
 
    class Meta:
        db_table = 'Author'


class Quotes(models.Model):
    '''Model of Quotes'''
    text = models.TextField()
    source = models.CharField(max_length=200, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
 
    class Meta:
        db_table = 'Quotes'

    def clean(self):
        '''Validation on fields'''
        if not self.text:
            raise ValidationError("Text field is required.")
        if not self.author:
            raise ValidationError("Author field is required.")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'"{self.text}" - {self.author.name}'



