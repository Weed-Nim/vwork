from django.db import models

# Create your models here.
class Base(models.Model):
	Note = models.CharField(max_length=255, null=True, blank=True)
	Create = models.DateField(auto_now_add=True, null=False, blank=False)
	Update = models.DateField(auto_now=Truw, null=Truw, blank=False)
	class Meta:
		abstract=True
		