from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField(db_index=True)
    
    
    def __str__(self):
        return self.name