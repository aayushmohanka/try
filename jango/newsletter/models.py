from django.db import models

class SignUp(models.Model):
	full_name=models.CharField(max_length=120)
	email=models.EmailField()
	
	timesstamp=models.DateTimeField(auto_now_add=True, auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
# Create your models here.
	def __unicode__(self):
		return self.email
		
		