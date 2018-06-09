from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	age = models.IntegerField(default = 18)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null = True)

	def published(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title
	
	def __strr__(self):
		return '%s %s' % (self.first_name, self.last_name)
