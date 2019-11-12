from django.db import models

# Create your models here.
class Table(models.Model):
    title = models.TextField()
    content = models.TextField()
    create_date = models.DateTimeField()
    actual_date = models.DateTimeField()
    columns = models.ManyToManyField('Column')

    def __str__(self): return self.title

class Column(models.Model):
    CHOICES = (
        ('b', 'Boolean'),
        ('i', 'Integer'),
        ('f', 'Float'),
        ('c', 'Char'),
        ('s', 'String'),
        ('d', 'DateTime')
    )
    name = models.TextField()
    description = models.TextField()
    datatype = models.CharField(max_length=1, choices=CHOICES)

    def __str__(self): return self.name + " (" + self.datatype + ")"