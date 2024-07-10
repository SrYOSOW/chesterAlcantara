from django.db import models



class Register(models.Model):
    fname = models.CharField(max_length=200)
    email = models.EmailField()
    mssg = models.TextField()

    def __str__(self):
        return self.email