from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #this sets the reltionship between posts and authors, called a 'one to many' relationship
    #by saying 'on_delete = models.CASCADE' we are saying that 'on the deletion of a user, delete all their entries too'
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} | {self.date_posted}'