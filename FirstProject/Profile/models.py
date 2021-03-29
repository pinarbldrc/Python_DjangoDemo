from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField("auth.User",on_delete=models.CASCADE)
    bio=models.TextField(max_length=100)
    city=models.CharField(max_length=50)
   # @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

        instance.profile.save()    

    post_save.connect(create_profile,sender="auth.User")    
# Create your models here.
