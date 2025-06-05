from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date = models.IntegerField()
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name
    
class Artists(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name