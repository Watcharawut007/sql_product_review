from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=200)
    Catagories = models.CharField(max_length=100)
class review(models.Model):
    rating_score = [1,2,3,4,5]
    review_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    comment_text = models.CharField(max_length=1000)
    rating = models.IntegerField(default=1,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    product =  models.ForeignKey(product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

