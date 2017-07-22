# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    writer = models.CharField(max_length = 50)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    active = models.BooleanField(default = True)
    inventory = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    book_format = models.CharField(max_length=150, default="Hard Copy")

    def get_absolute_url(self):
        return reversel("books:detail", args=[str(self.id)])
            #return reverse(books:detail", kwargs={"pk":self.pk})
            #return reverse(books:detail", args=[str(self.pk)})

#2.9 changes here 

def __str__(self):
    return ("%s, %s" % (self.book, self.book_format))

#Bring back a sale price if it exists
    def get_price(self):
        if self.sale_price is not None:
            return self.sale_price
        else:
            return self.price
    

#Old Changes
#    def __str__(self):
#      return self.title

    
