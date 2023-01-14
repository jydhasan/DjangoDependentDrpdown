from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title