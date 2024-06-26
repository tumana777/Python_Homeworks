from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "post"
        verbose_name_plural = "post"
        
    def __str__(self):
        return self.title