from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()
    salary=models.IntegerField()
    emp_id=models.CharField(max_length=100)


    def _str_(self):
        return self.firstname


class management(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    emp_id = models.CharField(max_length=100)

    def _str_(self):
        return self.emp_id