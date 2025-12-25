from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    duration = models.IntegerField()
    course_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.course_name
    

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=200)
    expertise = models.CharField(max_length=100)
    trainer_photo = models.ImageField(upload_to='images/trainers/')

    def __str__(self):
        return self.first_name + self.last_name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=200)
    is_active = models.BooleanField(default=True)
    entrolled_course = models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    trainer = models.ForeignKey(Trainer,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


