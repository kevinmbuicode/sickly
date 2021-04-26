from django.db import models

# Create your models here.
class user(models.Model):
	Name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class info(models.Model):
	lastname = models.ForeignKey(user, on_delete=models.CASCADE)
	country = models.CharField(max_length=30)
	subject = models.TextField(max_length=3000)