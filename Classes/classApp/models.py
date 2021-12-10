from django.db import models

#   Create your models here.
#   Creates class for dB
class djangoClasses(models.Model):
    Title = models.CharField(max_length=100, blank=False)
    Course_Number = models.IntegerField(unique=True)
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.Title

#   Creates three objects from djangoClasses and saves it
#   A = djangoClasses(Title='English', Course_Number=1, Instructor_Name ='Timothy', Duration=1)
#   A.save()
#   B = djangoClasses(Title='Math', Course_Number=2, Instructor_Name ='Jolene', Duration=1)
#   B.save()
#   C = djangoClasses(Title='Science', Course_Number=3, Instructor_Name ='Jake', Duration=1)
#   C.save()

