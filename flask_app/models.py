from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Posts(models.Model):
 #__bind_key__ = 'my_sql1'
 #__tablename__ = 'whposts'
# id = db.Column(db.Integer,primary_key=True)
 #wposts = db.Column(db.Text) 
 	id = models.IntegerField()
 	wposts=models.TextField()



 	def __str__(self):
 		return self.title