# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class mymodel(models.Model):
    name = models.CharField(max_length=50)
    major = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    def __str__(self):
        return self.name
