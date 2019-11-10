from django.db import models

# Create your models here.


class Post(models.Model):
	author = models.CharField(max_length=100)
	title = models.CharField(max_length=50)
	post_text = models.TextField()
	publish_date = models.DateTimeField()

	def __str__(self):
		final_title = self.title + ": author-" + self.author
		return final_title

class Comment(models.Model):
	author_of_comment = models.CharField(max_length=100)
	title = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.TextField()