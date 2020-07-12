from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return """
        Title      :\t {}\n
        Desc       :\t {}\n
        Created at :\t {}\n
        """.format(self.title,self.desc,self.created_at)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User,null= True,blank=True, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=255,default=1)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username