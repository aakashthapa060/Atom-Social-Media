from django.core import validators
import random
import math
from django.db import models
from django.core.validators import MaxLengthValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

def random_quote():
    quote = [
    "I’m the exception",
     "Simple but significant",
     "☕Stressed, blessed, and coffee obsessed ☕",
     "Sassy, classy with a touch of badassy",
     "Rollin’ with the homies",
     "Don’t kale my vibe",
     "🌟Sending my selfies to NASA because I’m a star 🌟",
     "Status Update: Currently hungry 🍔🍟🌭🌮🥗🍪",
     "Don’t study me. You won’t graduate 🎓"
     ]

    random_num =random.randint(0,8)
    randomQuote = quote[random_num]

    return randomQuote

     
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    profile_pic = models.ImageField(default = "default.jpg", upload_to = "profile_picture", blank = True,null = True)
    user_bio = models.TextField(validators = [MaxLengthValidator(300)], default= random_quote(), null = True, blank=True)
    following = models.ManyToManyField(User, related_name="following",blank = True)
    follower = models.ManyToManyField(User, related_name="follower",blank = True)

    @receiver(post_save,sender = User)
    def create_user_profile(sender,instance, created, **kwargs):
        if created:
            Profile.objects.create(user = instance)
    
    @receiver(post_save, sender = User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    
    def following_count(self):
        return self.following.count()
    
        
    def follower_count(self):
        return self.follower.count()

    def __str__(self):
        return f"{self.user} / profile"
    

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)
        width, height = img.size  # Get dimensions

        if width > 400 and height > 400:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 400 and height > 400:
            img.thumbnail((400, 400))

        img.save(self.profile_pic.path)


class SocialMediaLink(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    instagram_link = models.URLField(max_length=200, null=True, blank=True)
    facebook_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.profile} links"
    
    @receiver(post_save, sender= Profile)
    def create_social_media_link(sender, instance, created, **kwargs):
        if created:
            SocialMediaLink.objects.create(profile = instance)

    @receiver(post_save, sender = Profile)
    def save_social_meida_link(sender,instance, **kwargs):
        instance.socialmedialink.save()