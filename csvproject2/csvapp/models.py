from django.db import models
class Product(model.Model):
	no=models.IntegerField()
	name=models.CharField(max_length=64)
	price=models.IntegerField()
	warrenty=models.CharField(max_length=100)
	stock=models.IntegerField()
	