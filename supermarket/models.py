from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)
    is_sub_category = models.BooleanField(default = False)

    def __str__(self):
        return self.name

class Items(models.Model):
    name = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)
    amount = models.IntegerField(default = 0)
    category = models.ForeignKey(Category, related_name = 'category')
    sub_category = models.ForeignKey(Category, null = True, related_name = 'sub_category')

    def __str__(self):
        return self.name


        

