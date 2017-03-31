from django.db import models
from markdown_deux import markdown
#from django_markdown.widgets import MarkdownWidget #markdown

class Post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()
        #text = markdown(body)

	def _unicode__(self):
                return self.title




# class MyCustomForm(forms.Form):
#     content = forms.CharField(widget=MarkdownWidget())
