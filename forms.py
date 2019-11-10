from django import forms
from .models import Post, Comment

class New_Post(forms.ModelForm):
	class Meta:
		model = Post
		fields = ("title", "post_text","author")

class Add_comment(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("title", "author_of_comment", "text")