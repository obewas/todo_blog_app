from django.db import models

# Create your models here.
class Task(models.Model):
	taskName = models.CharField(max_length=250)
	description = models.TextField()
	is_done = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.taskName

