from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	body = models.TextField()
	created_at = models.DateField(auto_now = True)

	def to_json(self):
		return {
	      'id': self.id,
	      'title': self.title,
	      'body': self.body,
	      'created_at': self.created_at,
	    }

	def __str__(self):
		return self.title

	
