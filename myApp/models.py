from django.db import models



class Register(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    mssge = models.TextField()

    def __str__(self):
        return self.email