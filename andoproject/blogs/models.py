from django.db import models

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
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)