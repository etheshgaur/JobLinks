from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')  # Image field for storing the profile image
    bio = models.TextField(blank=True)
    social_media = models.URLField(null=True, blank=True) 

    def __str__(self):
        return self.title

class Link(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=100)
    visit_count = models.PositiveIntegerField(default=0)
    click_count = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.title