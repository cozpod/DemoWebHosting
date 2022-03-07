from tkinter import CASCADE
from turtle import position
from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    FathertName = models.CharField(max_length=100)
    MotherName = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

 