from django.db import models

# Create your models here.
class Kickstarter(models.Model):
    backers_count = models.IntegerField()
    name = models.CharField(max_length = 130)

#Add different data types