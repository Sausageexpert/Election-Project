from django.db import models

# Create your models here.

class Candidates(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=1000)
    votes = models.IntegerField(default = 0)
    picture = models.ImageField(default = 'profilepic.jpg', upload_to='candidate_pictures')
    
